# import awswrangler as wr
import argparse
import time
import requests

SEARCH_RESULT_LIMIT = 100000
SEARCH_FETCH_LIMIT = 500
TIMEOUT = (30, 300)


class SpySQLConnection:
    def __init__(
        self,
        api_url: str,
        api_key: str,
        org_uid: str,
        start_time: int,
        end_time: int,
    ):
        self.api_url = api_url
        self.api_key = api_key
        self.org_uid = org_uid
        self.start_time = int(start_time)
        self.end_time = int(end_time)
        self.sql_api_host = None

    def _initialize_sql_api_host(self):
        if self.sql_api_host is not None:
            return
        url = f"{self.api_url}/api/v1/org/{self.org_uid}/type"
        response = requests.get(
            url, headers={"Authorization": f"Bearer {self.api_key}"}
        )
        if response.status_code != 200:
            raise ValueError(
                f"Failed to resolve stack for SQL API host: {response.text}"
            )
        r = response.json()
        stack = r.get("policy", {}).get("processing_stack")
        if stack is None:
            raise ValueError(
                f"Failed to resolve stack for SQL API host: {response.text}"
            )
        self.sql_api_host = (
            f"http://athena-{stack}-service.{stack}.svc.cluster.local"
        )

    def cursor(self, **query_args):
        return SpySQLCursor(self, query_args)


class SpySQLCursor:
    def __init__(self, connection: SpySQLConnection, query_args: dict):
        self.connection = connection
        self.query_args = query_args
        if self.query is None:
            raise ValueError("Query is required")
        self.search_id = None
        self.status = "new"
        self.token = None
        self.result_count = 0
        self.results_received = 0
        self.error = None

    @property
    def query(self):
        return self.query_args.get("query")

    @property
    def query_type(self):
        if "select" in self.query.lower():  # type: ignore
            return "SQL"
        else:
            return "SPYQL"

    def execute(self):
        if self.query_type == "SQL":
            self._execute_sql()
        else:
            self._execute_spyql()

    def _execute_spyql(self):
        if self.search_id is not None:
            raise ValueError("Search already in progress")
        url = f"{self.connection.api_url}/api/v1/org/{self.connection.org_uid}/search/"
        for arg in ["schema", "query"]:
            if arg not in self.query_args:
                raise ValueError(
                    f"Missing required {arg} argument for spyql query"
                )
        data = {
            "schema": self.query_args["schema"],
            "query": self.query,
            "start_time": self.connection.start_time,
            "end_time": self.connection.end_time,
        }
        for kw in ["order_by", "group_by", "output_fields"]:
            if kw in self.query_args:
                data[kw] = self.query_args[kw]
        limit = self.query_args.get("limit", SEARCH_RESULT_LIMIT)
        params = {"limit": limit}
        response = requests.post(
            url,
            json=data,
            headers={"Authorization": f"Bearer {self.connection.api_key}"},
            params=params,
            timeout=TIMEOUT,
        )
        if response.status_code != 200:
            raise ValueError(f"Failed to execute query: {response.text}")
        try:
            r = response.json()
            if "error" in r:
                raise ValueError(r["error"])
            self.search_id = r["id"]
        except requests.exceptions.JSONDecodeError:
            raise ValueError(
                f"Failed to decode JSON response: {response.text}"
            )

    def _execute_sql(self):
        if self.search_id is not None:
            raise ValueError("Search already in progress")
        if self.connection.sql_api_host is None:
            self.connection._initialize_sql_api_host()
        url = f"{self.connection.sql_api_host}/directSQL"
        query = self.query
        if (params := self.query_args.get("params")) is not None:
            for k, v in [
                ("start_time", self.connection.start_time),
                ("end_time", self.connection.end_time),
            ]:
                if k not in params:
                    params[k] = v
            params["org_uid"] = self.connection.org_uid
            query = query.format(**params)
        data = {
            "org_uid": self.connection.org_uid,
            "schema": "n/a",
            "query": query,
            "start_time": self.connection.start_time,
            "end_time": self.connection.end_time,
        }

        response = requests.post(
            url,
            json=data,
            timeout=TIMEOUT,
        )
        if response.status_code != 200:
            raise ValueError(f"Failed to execute query: {response.text}")
        try:
            r = response.json()
            self.search_id = r["id"]
        except requests.exceptions.JSONDecodeError:
            raise ValueError(
                f"Failed to decode JSON response: {response.text}"
            )
        except KeyError as e:
            raise ValueError(
                f"Failed to execute query: {response.text} missing key {e}"
            )

    def _get_next_batch(self) -> list[dict]:
        if self.search_id is None:
            raise ValueError("No search in progress")
        url = f"{self.connection.api_url}/api/v1/org/{self.connection.org_uid}/search/{self.search_id}"
        data = {
            "limit": self.query_args.get("fetch_limit", SEARCH_FETCH_LIMIT)
        }
        if self.token is not None:
            data["token"] = self.token

        response = requests.post(
            url,
            json=data,
            headers={"Authorization": f"Bearer {self.connection.api_key}"},
            timeout=TIMEOUT,
        )
        if response.status_code != 200:
            raise ValueError(f"Failed to fetch results: {response.text}")

        try:
            r = response.json()
            if "status" in response.json():
                self.status = r["status"]
                self.error = r.get("error")
                return []
            else:
                self.status = "succeeded"
                self.error = None
                self.token = r.get("token")
                self.result_count = r.get("result_count", 0)
                return r["results"]
        except requests.exceptions.JSONDecodeError:
            raise ValueError(
                f"Failed to decode JSON response: {response.text}"
            )
        except KeyError as e:
            raise ValueError(
                f"Failed to fetch query response: {response.text} missing key {e}"
            )

    def done(self) -> bool:
        if self.status != "succeeded":
            return False
        return self.results_received >= self.result_count

    def progress(self) -> float:
        if self.status != "succeeded":
            return 0.0
        if self.result_count == 0:
            return 1.0
        return self.results_received / self.result_count

    def fetch_next(self) -> list[dict]:
        results = self._get_next_batch()
        while self.status == "still running":
            time.sleep(0.1)
            results = self._get_next_batch()
        if self.error is not None:
            raise ValueError(f"Search failed: {self.error}")
        self.results_received += len(results)
        return results

    def fetchall(self):
        results = []
        while not self.done():
            results.extend(self.fetch_next())
        return results


def parse_args():
    parser = argparse.ArgumentParser(description="Athena Query Executor")
    parser.add_argument(
        "--query", type=str, required=True, help="SQL query to execute"
    )
    parser.add_argument(
        "--org", type=str, required=True, help="Organization identifier"
    )
    parser.add_argument(
        "--start",
        type=int,
        required=True,
        help="Start of query time interval (timestamp)",
    )
    parser.add_argument(
        "--end",
        type=int,
        required=True,
        help="End of the query time interval (timestamp)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    api_url = os.getenv("API_URL")
    api_key = os.getenv("API_KEY")
    connection = SpySQLConnection(
        api_url=api_url,
        api_key=api_key,
        org_uid=args.org,
        start_time=args.start,
        end_time=args.end,
    )
    cursor = connection.cursor(query=args.query)
    cursor.execute()
    results = cursor.fetchall()
    print(results)


join_query = """
select event_redflag.id as rf_id, event_redflag.severity, event_redflag.short_name, event_redflag.traces, model_spydertrace.id as tr_id, model_spydertrace.score
from event_redflag cross join unnest(event_redflag.traces) as u(trace_id), model_spydertrace
where trace_id=model_spydertrace.id and model_spydertrace.score > 50 limit 20
"""

if __name__ == "__main__":
    import os

    main()
