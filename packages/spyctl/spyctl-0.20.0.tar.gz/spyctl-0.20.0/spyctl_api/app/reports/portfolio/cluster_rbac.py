from datetime import datetime, timezone
from pathlib import Path
import json
import spyctl.api.athena_search as search_api
import pandas as pd
from app.reports.reporter import Reporter, _basedir
import app.reports.mdx_lib as mdx_lib

s_org = "model_organization"
k8s_redflag_schemas = [
    "event_redflag:k8s_role_detection:1.1.0",
    "event_redflag:k8s_clusterrole_detection:1.1.0",
    "event_k8s_rolebinding_detection:1.1.0",
    "event_k8s_clusterrolebinding_detection:1.1.0",
    "event_redflag:new_k8s_serviceaccount_detected:1.1.0",
    "event_redflag:new_k8s_role_detected:1.1.0",
    "event_redflag:new_k8s_clusterrole_detected:1.1.0",
    "event_redflag:deleted_k8s_serviceaccount:1.1.0",
    "event_redflag:deleted_k8s_role:1.1.0",
    "event_redflag:deleted_k8s_clusterrole:1.1.0",
    "event_redflag:k8s_role_drift:1.1.0",
]

aws_redflag_schemas = [
    "event_redflag:iam_role_trust_policy_drift:1.1.0",
    "event_redflag:iam_role_permissions_drift:1.1.0",
    "event_redflag:new_aws_iam_role_detected:1.1.0",
    "event_redflag:aws_iam_role_deleted:1.1.0",
]


def summarize_k8s_rules(rules: list) -> list:
    if rules is None or isinstance(rules, float):
        return [""]
    return [summarize_k8s_rule(rule) for rule in rules]


def summarize_k8s_rule(rule: dict) -> str:
    api_groups = group_to_str(rule.get("apiGroups", []))
    resources = group_to_str(rule.get("resources", []))
    verbs = group_to_str(rule.get("verbs", []))
    rv = ""
    if api_groups:
        rv += f"{api_groups} -"
    if verbs:
        rv += f" {verbs} -"
    if resources:
        rv += f" {resources}"

    return rv


def group_to_str(group: list) -> str:
    rv = ""
    if not group:
        return ""
    if isinstance(group, str):
        return group
    if len(group) == 1:
        return group[0]
    for g in group[:-1]:
        if g:
            rv += f"{g}, "
    if group[-1]:
        rv += f"{group[-1]}"
    return rv


def summarize_attached_policies(policies: list) -> list:
    if policies is None or isinstance(policies, float):
        return [""]
    return [
        summarize_statement(statement)
        for policy in policies
        for statement in get_attached_policy_statements(policy)
    ]


def get_attached_policy_statements(policy: dict) -> list:
    return (
        policy.get("default_version", {})
        .get("policy", {})
        .get("Document", {})
        .get("Statement", [])
    )


def summarize_inline_policies(policies: list) -> list:
    if policies is None or isinstance(policies, float):
        return [""]
    return [
        summarize_statement(statement)
        for policy in policies
        for statement in policy.get("Statement", [])
    ]


def summarize_aws_policies(row) -> list:
    inline_summary = summarize_inline_policies(
        row.get("aws_inline_policies", [])
    )
    attached_summary = summarize_attached_policies(
        row.get("aws_attached_policies", [])
    )
    if not inline_summary:
        return attached_summary
    if not attached_summary:
        return inline_summary
    return inline_summary + attached_summary


def summarize_statement(statement: dict) -> str:
    effect = statement.get("Effect", "")
    actions = group_to_str(statement.get("Action", []))
    resources = group_to_str(statement.get("Resource", []))
    return f"{effect} - {actions} on: {resources}"


class RbacReporter(Reporter):

    def __init__(self, spec: dict):
        super().__init__(spec)
        self.error = {}
        self.context = {}

    def collect_and_process(
        self,
        args: dict[str, str | float | int | bool],
        org_uid: str,
        api_key: str,
        api_url: str,
    ):
        end = time = int(args["time"])
        start = time - 7200
        self.context["time"] = time

        cluid = args.get("cluid")

        k8s_data = []
        cluster = search_api.search_athena(
            api_url,
            api_key,
            org_uid,
            schema="model_k8s_cluster",
            query=f'id="{cluid}"',
            start_time=start,
            end_time=end,
            use_pbar=False,
            quiet=True,
        )

        k8s_data += cluster

        for schema in [
            "model_k8s_role",
            "model_k8s_rolebinding",
            "model_k8s_clusterrole",
            "model_k8s_clusterrolebinding",
            "model_k8s_serviceaccount",
            "model_k8s_deployment",
            "model_k8s_daemonset",
            "model_k8s_statefulset",
        ]:
            data = search_api.search_athena(
                api_url,
                api_key,
                org_uid,
                schema=schema,
                query=f'cluster_uid="{cluid}"',
                start_time=start,
                end_time=end,
                use_pbar=False,
                quiet=True,
            )
            k8s_data += data

        df = pd.DataFrame(k8s_data)

        schema_condition = " or ".join(
            [f'original_schema="{schema}"' for schema in k8s_redflag_schemas]
        )
        query = f'cluster_uid="{cluid}" and ({schema_condition})'
        df_flags = pd.DataFrame(
            search_api.search_athena(
                api_url,
                api_key,
                org_uid,
                schema="event_redflag",
                query=query,
                start_time=start,
                end_time=end,
                use_pbar=False,
                quiet=True,
            )
        )

        if df.empty:
            self.error = {
                "error": {
                    "message": "It looks like there is currently no Kubernetes data available for this cluster for the selected time."
                }
            }
            return

        # Get the cluster model to get the cluster name
        cluster_name = ""
        clusters = df[df.kind == "Cluster"]
        if not clusters.empty:
            cluster_name = clusters.name.iloc[0]
        self.context["cluster_name"] = cluster_name

        # Process the kubernetes data

        # Extract service account, name and namespace as separate columns
        df["service_account"] = pd.json_normalize(df.spec)[
            "template.spec.serviceAccount"
        ]
        df[["name", "namespace"]] = pd.json_normalize(df.metadata)[
            ["name", "namespace"]
        ]

        # Extract all roles, service accounts and role bindings in separate dataframes for joining

        # Service accounts first
        serviceAccounts = (
            df[df.kind == "ServiceAccount"].reset_index(drop=True).copy()
        )
        svc_acc_cols = [
            "id",
            "name",
            "namespace",
            "kind",
            "metadata",
            "aws_role_arn",
            "aws_role_uid",
            "status",
        ]
        if "aws_role_arn" not in serviceAccounts.columns:
            serviceAccounts["aws_role_arn"] = ""
        if "aws_role_uid" not in serviceAccounts.columns:
            serviceAccounts["aws_role_uid"] = ""

        # Kubernetes roles and cluster roles
        roles = (
            df[(df.kind == "Role") | (df.kind == "ClusterRole")]
            .reset_index(drop=True)
            .copy()
        )
        role_cols = ["id", "kind", "name", "namespace", "rules", "status"]

        # Find any service accounts with associated AWS IAM roles and make list of all aws account ids
        iam_cols_initial = [
            "id",
            "arn",
            "RoleName",
            "AssumeRolePolicyDocument",
            "inline_policies",
            "attached_role_policies",
            "status",
        ]
        iam_roles = pd.DataFrame(columns=iam_cols_initial)

        if "aws_account_id" in serviceAccounts.columns:
            aws_accounts = serviceAccounts.aws_account_id.dropna().unique()

            # See if we can pull the IAM roles for that account (if an aws agent is pulling that info)

            iam_roles = pd.DataFrame()
            for account_id in aws_accounts:
                aws_data = search_api.search_athena(
                    api_url=api_url,
                    api_key=api_key,
                    org_uid=org_uid,
                    schema="model_aws_iam_role",
                    query=f'aws_account_id="{account_id}"',
                    start_time=start,
                    end_time=end,
                    use_pbar=False,
                    quiet=True,
                )
                iam_roles = pd.concat([iam_roles, pd.DataFrame(aws_data)])

                # TODO Get iam flags here

            if not iam_roles.empty:
                iam_roles = (
                    iam_roles[iam_cols_initial].reset_index(drop=True).copy()
                )
                iam_roles.rename(
                    columns={"status": "iam_role_status"}, inplace=True
                )

        iam_cols = [
            "id",
            "arn",
            "RoleName",
            "AssumeRolePolicyDocument",
            "inline_policies",
            "attached_role_policies",
            "iam_role_status",
        ]

        # Get the role bindings - which provide the many to many mapping between roles and service accounts
        bindings = (
            df[(df.kind == "RoleBinding") | (df.kind == "ClusterRoleBinding")]
            .reset_index(drop=True)
            .copy()
        )
        # then get only required subject and roleRef fields
        bindings["role_uid"] = pd.json_normalize(bindings["roleRef"])[
            "role_uid"
        ]
        # Need to explode subject_uids cause they can reference multiple subjects.
        bindings = bindings.explode("subject_uids").reset_index(drop=True)
        bindings.rename(columns={"subject_uids": "subject_uid"}, inplace=True)

        binding_cols = [
            "role_uid",
            "subject_uid",
        ]

        # Now we can join it all up to get full picture

        # Merge bindings to roles
        merged1 = pd.merge(
            left=bindings[binding_cols],
            right=roles[role_cols],
            left_on=["role_uid"],
            right_on=["id"],
            how="left",
        )
        merged1.drop(columns=["id"], inplace=True)
        merged1.rename(
            columns={
                "kind": "role_kind",
                "name": "role_name",
                "namespace": "role_namespace",
                "status": "role_status",
            },
            inplace=True,
        )

        # Merge bindings to service accounts
        merged2 = pd.merge(
            left=merged1,
            right=serviceAccounts[svc_acc_cols],
            left_on=["subject_uid"],
            right_on=["id"],
            how="right",
        ).rename(
            columns={"id": "svc_account_uid", "status": "svc_account_status"}
        )

        # account_to_k8s maps a service account to its associated roles and
        # their rbac rules
        account_to_k8srules = merged2[
            [
                "kind",
                "name",
                "namespace",
                "svc_account_uid",
                "svc_account_status",
                "aws_role_arn",
                "aws_role_uid",
                "role_uid",
                "role_name",
                "rules",
                "role_status",
            ]
        ].copy()

        # Now merge in with the IAM roles, if we have any
        account_to_rules = pd.merge(
            left=account_to_k8srules,
            right=iam_roles,
            left_on="aws_role_arn",
            right_on="arn",
            how="left",
        )
        account_to_rules.rename(
            columns={
                "kind": "svc_account_kind",
                "name": "svc_account_name",
                "namespace": "svc_account_namespace",
                "RoleName": "aws_role_name",
                "AssumeRolePolicyDocument": "aws_assume_role_policy",
                "inline_policies": "aws_inline_policies",
                "attached_role_policies": "aws_attached_policies",
            },
            inplace=True,
        )

        # Summarize the rbac rules and permissions
        account_to_rules["rules_summary"] = account_to_rules.rules.apply(
            lambda x: summarize_k8s_rules(x)
        )
        account_to_rules["aws_permissions"] = account_to_rules.apply(
            summarize_aws_policies, axis=1
        )

        # Merge the resources with service accounts to the service account rbac summary
        # We do a last-model here on the resources in case there are multiple versions of the same resource
        resources = (
            df[df.service_account.notnull()]
            .groupby(["kind", "name", "namespace", "service_account"])
            .last()
            .reset_index()
            .copy()
        )
        res_cols = ["id", "kind", "name", "namespace", "service_account"]
        rules_cols = [
            "svc_account_uid",
            "svc_account_kind",
            "svc_account_namespace",
            "svc_account_name",
            "svc_account_status",
            "role_uid",
            "role_name",
            "rules_summary",
            "role_status",
            "aws_role_arn",
            "aws_role_name",
            "aws_assume_role_policy",
            "aws_permissions",
            "iam_role_status",
        ]
        df_rbac = pd.merge(
            left=resources[res_cols],
            right=account_to_rules[rules_cols],
            left_on=["service_account", "namespace"],
            right_on=["svc_account_name", "svc_account_namespace"],
            how="left",
        )

        df_rbac.rename(
            columns={"rules_summary": "k8s rbac permissions"}, inplace=True
        )
        df_rbac[
            [
                "role_name",
                "aws_role_arn",
                "aws_role_name",
                "aws_assume_role_policy",
            ]
        ] = df_rbac[
            [
                "role_name",
                "aws_role_arn",
                "aws_role_name",
                "aws_assume_role_policy",
            ]
        ].fillna(
            ""
        )

        self.rbac_analysis = df_rbac

        self.context.update(
            {
                "rbac_analysis": self.rbac_analysis,
            }
        )

        # Now enrich the flags with context on which they apply

        # Flags on roles
        role_flag_cols = [
            "time",
            "cluster_name",
            "schema",
            "short_name",
            "severity",
            "description",
            "impact",
            "content",
            "name",
            "namespace",
            "service_account",
            "role_name",
        ]
        role_flags = pd.DataFrame(columns=role_flag_cols)
        if len(df_flags) > 0:
            role_flags = (
                df_flags.merge(df_rbac, left_on="ref", right_on="role_uid")
                .groupby(role_flag_cols)
                .last()
                .sort_values(by="time", ascending=False)
                .reset_index()
            )

        # Flags on service accounts
        svc_acc_flag_cols = [
            "time",
            "cluster_name",
            "schema",
            "short_name",
            "severity",
            "description",
            "impact",
            "content",
            "name",
            "namespace",
            "service_account",
        ]
        svc_acc_flags = pd.DataFrame(columns=role_flag_cols)
        if len(df_flags) > 0:
            svc_acc_flags = (
                df_flags.merge(df_rbac, left_on="ref", right_on="svc_account_uid")
                .groupby(svc_acc_flag_cols)
                .last()
                .sort_values(by="time", ascending=False)
                .reset_index()
            )
        self.context["role_flags"] = role_flags
        self.context["svc_acc_flags"] = svc_acc_flags

    def renderer(self, fmt: str, rid: str) -> Path:

        if self.error:
            return self.render(self.error, fmt, rid)

        if fmt == "mdx":
            mdx_context = self.make_mdx_context(self.context)
            return self.render(mdx_context, fmt, rid)
        if fmt == "xlsx":
            # Remove time and cluster name from context
            # so the excel writer doesn't try to make these into
            # separate sheets
            xlsx_context = {"rbac_analysis": self.rbac_analysis}
            return self.render(xlsx_context, fmt, rid)
        else:
            return super().renderer(fmt, rid)

    def make_mdx_context(self, context: dict) -> dict:

        mdx_ctx = {}
        mdx_ctx["cluster_name"] = context["cluster_name"]
        mdx_ctx["time"] = (
            datetime.fromtimestamp(context["time"], timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S %Z"
            ),
        )

        k8s_data_cols = ["role_name", "k8s rbac permissions"]
        k8s_rename_cols = ["Role Name", "Role Permissions"]
        k8s_perms = k8s_rename_cols[-1]

        aws_data_cols = ["aws_role_name", "aws_permissions"]
        aws_rename_cols = [
            "Associated IAM Role",
            "AWS Role Permissions",
        ]
        aws_perms = aws_rename_cols[-1]

        mdx_ctx["resources"] = []
        for namespace, namespace_data in self.rbac_analysis.groupby(
            "namespace"
        ):
            ns_data = []
            for kind_name_acct, data in namespace_data.groupby(
                ["kind", "name", "service_account"]
            ):
                rv = dict()
                rv["kind"], rv["name"], rv["service_account"] = kind_name_acct
                rv["has_k8s_role"] = not data[data.role_name != ""].empty
                aws_data = data[
                    (data.aws_role_name != "")
                    & (data.iam_role_status != "closed")
                ][aws_data_cols]
                rv["has_aws_role"] = not aws_data.empty

                if rv["has_k8s_role"]:
                    k8s_data = data[data.role_status == "active"][
                        k8s_data_cols
                    ].rename(columns=dict(zip(k8s_data_cols, k8s_rename_cols)))
                    k8s_data = k8s_data.explode(k8s_perms)
                    rv["k8s_rbac_grid"] = mdx_lib.make_grid_df(
                        k8s_data,
                        grid_options={
                            "rowspanning": True,
                            "autoRowHeight": True,
                        },
                    )
                if rv["has_aws_role"]:
                    aws_data = aws_data.rename(
                        columns=dict(zip(aws_data_cols, aws_rename_cols))
                    )
                    aws_data = aws_data.explode(aws_perms)
                    rv["aws_rbac_grid"] = mdx_lib.make_grid_df(
                        aws_data,
                        grid_options={
                            "rowspanning": True,
                            "autoRowHeight": True,
                        },
                    )
                ns_data.append(rv)
            mdx_ctx["resources"].append(
                {"namespace": namespace, "data": ns_data}
            )
        if len(context["role_flags"]) > 0:
            render_cols = [
                "time",
                "description",
                "role_name",
                "service_account",
                "name",
                "namespace",
            ]
            mdx_ctx["flags"] = True
            mdx_ctx["role_flag_grid"] = mdx_lib.make_grid_df(
                df=context["role_flags"][render_cols],
                column_options={
                    "time": {"title": "Time", "type": "timestamp"},
                    "name": {"title": "Service Account Owner"},
                },
            )

        if len(context["svc_acc_flags"]) > 0:
            render_cols = [
                "time",
                "description",
                "service_account",
                "name",
                "namespace",
            ]
            mdx_ctx["flags"] = True
            mdx_ctx["svc_acc_flag_grid"] = mdx_lib.make_grid_df(
                df=context["svc_acc_flags"][render_cols],
                column_options={
                    "time": {"title": "Time", "type": "timestamp"},
                    "name": {"title": "Service Account Owner"},
                },
            )
        return mdx_ctx
