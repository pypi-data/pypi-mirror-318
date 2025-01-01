import sys
import traceback
import json
import logging
import time
from abc import ABC, abstractmethod
from collections import defaultdict
from pathlib import Path
import pandas as pd

import yaml
from jinja2 import Environment, PackageLoader

import app.reports.report_lib as rlib
from app.reports.report import Report

_basedir = "/tmp"
logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger("uvicorn")


class Reporter(ABC):
    def __init__(self, spec: dict):
        self.spec = spec
        self.context = {}

    def collector(
        self,
        args: dict[str, str | float | int | bool],
        org_uid: str,
        api_key: str,
        api_url: str,
    ) -> list:
        return []

    def processor(
        self,
        data: list,
        args: dict[str, str | float | int | bool | list],
    ) -> dict:
        return {}

    def collect_and_process(
        self,
        args: dict[str, str | float | int | bool],
        org_uid: str,
        api_key: str,
        api_url: str,
    ) -> None:

        # Get the data
        data = self.collector(
            args=args,
            org_uid=org_uid,
            api_key=api_key,
            api_url=api_url,
        )

        # Process the data to a lowest common denominator context
        # dict that can be used to render the report in multiple formats
        self.context = self.processor(data, args)

    def renderer(
        self,
        format: str,
        rid: str,
    ) -> Path:
        return self.render(self.context, format, rid)

    def generate_reports(
        self, r: Report, api_key: str, api_url: str
    ) -> dict[rlib.FORMATS, Path]:
        rv = dict()

        try:
            logger.info(
                f"Generating {r.input.report_id} report for {r.input.org_uid} ({r.id})"
            )
            t1 = time.time()

            # Collect and process the data
            self.collect_and_process(
                args=r.input.report_args,
                org_uid=r.input.org_uid,
                api_key=api_key,
                api_url=api_url,
            )

            t2 = time.time()
            logger.info(
                f"Collection and processing done for {r.input.report_id} "
                f"report for {r.input.org_uid} ({r.id}) - took {t2-t1} seconds"
            )

            # Render the report in all supported formats
            for fmt in self.spec["supported_formats"]:
                rv[fmt] = self.renderer(fmt, r.id)  # type: ignore

            t3 = time.time()
            logger.info(
                f"Rendering done for {r.input.report_id} report for {r.input.org_uid} ({r.id}) - took {t3-t2} seconds"
            )
        except Exception as e:
            logger.error(
                f"Error generating report {r.input.report_id} for {r.input.org_uid} ({r.id}): {e}"
            )
            traceback.print_exc()
            raise

        return rv

    def render(self, context: dict, format: str, rid: str) -> Path:

        if format == "json":
            to_dump = dict()
            for k, v in context.items():
                if isinstance(v, pd.DataFrame):
                    to_dump[k] = json.loads(
                        v.reset_index().to_json(orient="records")
                    )
                else:
                    to_dump[k] = v

            with open(f"{_basedir}/{rid}.json", "w") as f:
                json.dump(to_dump, f)
            return Path(f"{_basedir}/{rid}.json")

        if format == "yaml":
            # Yaml default dict output is adding in python info about
            # the default dict type and function, so we need to convert
            # the default dict to a normal dict before writing to yaml
            to_dump = dict()
            for k, v in context.items():
                if isinstance(v, pd.DataFrame):
                    to_dump[k] = json.loads(
                        v.reset_index().to_json(orient="records")
                    )
                if isinstance(v, defaultdict):
                    to_dump[k] = defaultdict_to_dict(v)
                else:
                    to_dump[k] = v
            with open(f"{_basedir}/{rid}.yaml", "w") as f:
                yaml.dump(to_dump, f)
            return Path(f"{_basedir}/{rid}.yaml")

        if format == "md":
            with open(f"{_basedir}/{rid}.md", "w") as f:
                f.write(self.render_with_template(format, context))
            return Path(f"{_basedir}/{rid}.md")

        if format == "mdx":
            with open(f"{_basedir}/{rid}.mdx", "w") as f:
                f.write(self.render_with_template(format, context))
            return Path(f"{_basedir}/{rid}.mdx")


        if format == "xlsx":
            outfile = Path(_basedir) / Path(f"{rid}.xlsx")
            with pd.ExcelWriter(outfile, engine="xlsxwriter") as writer:
                for k, v in context.items():
                    sheet_name = k.split("df_")[-1]
                    if isinstance(v, pd.DataFrame):
                        v.to_excel(writer, sheet_name=sheet_name, index=False)
                    elif isinstance(v, dict) or isinstance(v, str):
                        df = pd.DataFrame([v])
                        df.to_excel(writer, sheet_name=sheet_name, index=False)
                    elif isinstance(v, list):
                        df = pd.DataFrame(v)
                        df.to_excel(writer, sheet_name=sheet_name, index=False)
                    else:
                        logger.warning(
                            f"Excel export - Unsupported type {type(v)} for {k} in context, skipping"
                        )
                        continue
            return outfile

        raise ValueError(f"Unsupported format: {format}")

    def render_with_template(self, format, context):
        environment = Environment(
            loader=PackageLoader("app.reports.portfolio", "templates")
        )
        template_spec = self.spec["templates"][format]
        template = environment.get_template(template_spec)
        return template.render(context)


def defaultdict_to_dict(d):
    if isinstance(d, defaultdict):
        d = {k: defaultdict_to_dict(v) for k, v in d.items()}
    return d
