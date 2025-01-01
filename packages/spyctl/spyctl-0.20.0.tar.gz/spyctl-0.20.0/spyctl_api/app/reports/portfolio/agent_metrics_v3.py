import logging
import time
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

import app.reports.athena_lib as athena_lib
import app.reports.mdx_lib as mdx_lib
from app.reports.reporter import Reporter

_METRIC_KEYS = [
    "ref",
    "time",
    "mem_1min_B",
    "cpu_1min_P",
    "bandwidth_1min_Bps",
]

logger = logging.getLogger("uvicorn")


def metric_project(metric: dict) -> dict:
    return {k: metric[k] for k in _METRIC_KEYS}


class AgentMetricsReporter(Reporter):

    def __init__(self, spec: dict):
        super().__init__(spec)
        self.agents = []
        self.df = pd.DataFrame()
        self.error = {}
        self.context = {}

    def collect_and_process(
        self,
        args: dict[str, str | float | int | bool],
        org_uid: str,
        api_key: str,
        api_url: str,
    ) -> None:

        start_time = int(args["st"])
        now = time.time()
        if now - start_time < 60 * 60 * 2:
            start_time = now - 60 * 60 * 2
        end_time = int(args["et"])

        conn = athena_lib.SpySQLConnection(
            org_uid=org_uid,
            api_key=api_key,
            api_url=api_url,
            start_time=start_time,
            end_time=end_time,
        )
        query_by_agent = """
SELECT
    hostname,
    AVG("cpu_1min_p.agent") AS cpu_mean,
    approx_percentile("cpu_1min_p.agent", 0.9) AS cpu_p90,
    approx_percentile("cpu_1min_p.agent", 0.95) AS cpu_p95,
    AVG(bandwidth_1min_bps) AS network_mean,
    approx_percentile(bandwidth_1min_bps, 0.9) AS network_p90,
    approx_percentile(bandwidth_1min_bps, 0.95) AS network_p95,
    AVG("mem_1min_b.agent") AS mem_mean,
    approx_percentile("mem_1min_b.agent", 0.9) AS mem_p90,
    approx_percentile("mem_1min_b.agent", 0.95) AS mem_p95

FROM event_metric
WHERE original_schema='event_metric:agent:1.0.0' and cluster_name='{cluster_name}' and time >= {start_time} and time < {end_time}
GROUP BY
    hostname
"""
        cursor = conn.cursor(
            query=query_by_agent,
            params={
                "cluster_name": args["cluster"],
            },
        )
        cursor.execute()
        results = cursor.fetchall()
        df_by_agent = pd.DataFrame(results)

        if len(df_by_agent) == 0:
            self.error = {"error": {"message": "No data available"}}
            return

        self.context["df_by_agent"] = df_by_agent

        query_all = """
SELECT
    AVG("cpu_1min_p.agent") AS cpu_mean,
    approx_percentile("cpu_1min_p.agent", 0.9) AS cpu_p90,
    approx_percentile("cpu_1min_p.agent", 0.95) AS cpu_p95,
    AVG(bandwidth_1min_bps) AS network_mean,
    approx_percentile(bandwidth_1min_bps, 0.9) AS network_p90,
    approx_percentile(bandwidth_1min_bps, 0.95) AS network_p95,
    AVG("mem_1min_b.agent") AS mem_mean,
    approx_percentile("mem_1min_b.agent", 0.9) AS mem_p90,
    approx_percentile("mem_1min_b.agent", 0.95) AS mem_p95

FROM event_metric
WHERE original_schema='event_metric:agent:1.0.0' and cluster_name='{cluster_name}' and time >= {start_time} and time < {end_time}
"""
        cursor = conn.cursor(
            query=query_all,
            params={
                "cluster_name": args["cluster"],
            },
        )
        cursor.execute()
        results = cursor.fetchall()
        df_all = pd.DataFrame(results)

        if len(df_all) == 0:
            self.error = {"error": {"message": "No data available"}}
            return

        # Fill out the rest of the context
        # Cluster name
        self.context["cluster"] = {
            "name": args["cluster"],
        }

        self.context["start_time"] = int(start_time)
        self.context["end_time"] = int(end_time)

        # Export frames to dicts context
        self.context["metrics_summary"] = {
            "cpu": {
                "mean": float(df_all.cpu_mean.iloc[0]),
                "p90": float(df_all.cpu_p90.iloc[0]),
                "p95": float(df_all.cpu_p95.iloc[0]),
            },
            "mem": {
                "mean": float(df_all.mem_mean.iloc[0]),
                "p90": float(df_all.mem_p90.iloc[0]),
                "p95": float(df_all.mem_p95.iloc[0]),
            },
            "bps": {
                "mean": float(df_all.network_mean.iloc[0]),
                "p90": float(df_all.network_p90.iloc[0]),
                "p95": float(df_all.network_p95.iloc[0]),
            },
        }

    def renderer(
        self,
        fmt: str,
        rid: str,
    ) -> Path:
        if self.error:
            return self.render(self.error, fmt, rid)

        # For MDX format, we need to convert this to grid definitions to render
        if fmt == "mdx":
            # Export dataframes to mdx context
            mdx_context = self.make_mdx_context(self.context)
            return self.render(mdx_context, fmt, rid)
        else:
            return super().renderer(fmt, rid)

    def make_mdx_context(self, context: dict) -> dict:
        if "error" in context:
            return context
        mdx_context = deepcopy(context)
        mdx_context["start_time"] = datetime.fromtimestamp(
            context["start_time"], timezone.utc
        ).strftime("%Y-%m-%d %H:%M:%S %Z")
        mdx_context["end_time"] = datetime.fromtimestamp(
            context["end_time"], timezone.utc
        ).strftime("%Y-%m-%d %H:%M:%S %Z")
        summary_grid = self.make_summary_grid(context["metrics_summary"])
        mdx_context["metrics_summary_grid"] = summary_grid

        mdx_context["agent_metrics_cpu_grid"] = mdx_lib.make_grid_df(
            df=self.context["df_by_agent"][
                ["hostname", "cpu_mean", "cpu_p90", "cpu_p95"]
            ].round(
                {
                    "cpu_mean": 3,
                    "cpu_p90": 3,
                    "cpu_p95": 3,
                }
            ),
            column_options={
                "hostname": {"title": "Agent"},
                "cpu_mean": {"title": "Mean"},
                "cpu_p90": {"title": "P90"},
                "cpu_p95": {"title": "P95"},
            },
        )

        mdx_context["agent_metrics_mem_grid"] = mdx_lib.make_grid_df(
            df=self.context["df_by_agent"][
                ["hostname", "mem_mean", "mem_p90", "mem_p95"]
            ],
            column_options={
                "hostname": {"title": "Agent"},
                "mem_mean": {"title": "Mean", "type": "bytes"},
                "mem_p90": {"title": "P90", "type": "bytes"},
                "mem_p95": {"title": "P95", "type": "bytes"},
            },
        )

        mdx_context["agent_metrics_network_grid"] = mdx_lib.make_grid_df(
            df=self.context["df_by_agent"][
                ["hostname", "network_mean", "network_p90", "network_p95"]
            ],
            column_options={
                "hostname": {"title": "Agent"},
                "network_mean": {"title": "Mean", "type": "bytesPerSecond"},
                "network_p90": {"title": "P90", "type": "bytesPerSecond"},
                "network_p95": {"title": "P95", "type": "bytesPerSecond"},
            },
        )

        return mdx_context

    def make_summary_grid(self, summary: dict) -> str:
        columns = [
            {"title": "Metric", "field": "metric"},
            {
                "title": "Mean",
                "field": "mean",
            },
            {
                "title": "P90",
                "field": "p90",
            },
            {
                "title": "P95",
                "field": "p95",
            },
        ]
        data = [
            {
                "metric": "CPU load",
                "mean": round(summary["cpu"]["mean"], 3),
                "p90": round(summary["cpu"]["p90"], 3),
                "p95": round(summary["cpu"]["p95"], 3),
            },
            {
                "metric": "Memory (MB)",
                "mean": f'{round(summary["mem"]["mean"] / 1048576)} MB',
                "p90": f'{round(summary["mem"]["p90"] / 1048576)} MB',
                "p95": f'{round(summary["mem"]["p95"] / 1048576)} MB',
            },
            {
                "metric": "Bandwidth (bytes/sec)",
                "mean": f'{round(summary["bps"]["mean"])}',
                "p90": f'{round(summary["bps"]["p90"])}',
                "p95": f'{round(summary["bps"]["p95"])}',
            },
        ]
        return mdx_lib.make_grid(columns, data)
