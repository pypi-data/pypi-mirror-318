import os
import time

import pytest

import app.reports.athena_lib as athena_lib
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
ORG = os.getenv("ORG")
DO_INTEGRATED_TESTS = os.getenv("DO_INTEGRATED_TESTS") is not None


@pytest.fixture
def conn():
    end_time = int(time.time())
    start_time = end_time - 3600
    conn = athena_lib.SpySQLConnection(
        org_uid=os.getenv("ORG"),
        api_key=os.getenv("API_KEY"),
        api_url=os.getenv("API_URL"),
        start_time=start_time,
        end_time=end_time,
    )
    yield conn


def test_sql_fetch_all(conn):
    if not API_KEY or not API_URL or not ORG:
        pytest.skip("Skipping test without API_KEY, API_URL, ORG")
    if not DO_INTEGRATED_TESTS:
        pytest.skip("Skipping integration test")
    sql = "SELECT id, time FROM model_process limit 5"
    cursor = conn.cursor(query=sql)
    cursor.execute()
    rows = cursor.fetchall()
    assert len(rows) == 5
    for r in rows:
        assert r is not None
        assert "id" in r
        assert "time" in r


def test_sql_fetch_next(conn):
    if not API_KEY or not API_URL or not ORG:
        pytest.skip("Skipping test without API_KEY, API_URL, ORG")
    if not DO_INTEGRATED_TESTS:
        pytest.skip("Skipping integration test")
    sql = "SELECT id, time, muid FROM model_process limit 1000"
    cursor = conn.cursor(query=sql)
    cursor.execute()
    while not cursor.done():
        next = cursor.fetch_next()
        assert cursor.progress() > 0
        assert cursor.progress() <= 1
        assert len(next) == 500 or cursor.done() and len(next) < 500
        for r in next:
            assert r is not None
            assert "id" in r
            assert "time" in r
    assert cursor.progress() == 1


def test_spyql_fetch_all(conn):
    if not API_KEY or not API_URL or not ORG:
        pytest.skip("Skipping test without API_KEY, API_URL, ORG")
    if not DO_INTEGRATED_TESTS:
        pytest.skip("Skipping integration test")
    cursor = conn.cursor(
        query="*",
        schema="model_process",
        output_fields=["id", "time"],
        limit=100,
    )
    cursor.execute()
    rows = cursor.fetchall()
    assert len(rows) == 100
    for r in rows:
        assert r is not None
        assert "id" in r
        assert "time" in r


def test_spyql_fetch_next(conn):
    if not API_KEY or not API_URL or not ORG:
        pytest.skip("Skipping test without API_KEY, API_URL, ORG")
    if not DO_INTEGRATED_TESTS:
        pytest.skip("Skipping integration test")
    cursor = conn.cursor(
        query="*",
        schema="model_process",
        output_fields=["id", "time"],
        limit=105,
        fetch_limit=10
    )
    cursor.execute()
    nr_fetches = 0
    while not cursor.done():
        next = cursor.fetch_next()
        nr_fetches += 1
        assert cursor.progress() > 0
        assert cursor.progress() <= 1
        assert len(next) == 10 or cursor.done() and len(next) < 10
        for r in next:
            assert r is not None
            assert "id" in r
            assert "time" in r
    assert cursor.progress() == 1
    assert nr_fetches == 11


def test_agent_metrics(conn):
    if not API_KEY or not API_URL or not ORG:
        pytest.skip("Skipping test without API_KEY, API_URL, ORG")
    if not DO_INTEGRATED_TESTS:
        pytest.skip("Skipping integration test")
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
            "cluster_name": "integrationc2reinstall",
        },
    )
    cursor.execute()
    results = cursor.fetchall()
    assert len(results) > 0