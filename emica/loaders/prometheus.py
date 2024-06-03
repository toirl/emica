from datetime import UTC, datetime, timedelta
from typing import Dict

import requests

from emica.core.metrics import Instances, Metric, Metrics

queries = {
    "cpu_utilization": 'label_replace(100 * (1 - avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[60s]))), "metric", "cpu_utilization", "", "")',
    "memory_capacity": 'label_replace((node_memory_total_bytes/1024/1024/1024), "metric", "memory_capacity", "", "")',
    "memory_utilization": 'label_replace(((node_memory_active_bytes/1024/1024/1024)/(node_memory_total_bytes/1024/1024/1024)*100), "metric", "memory_utilization", "", "")',
}


class Query:
    def __init__(self):
        self.query = f"{queries["cpu_utilization"]} or {queries['memory_capacity']} or {queries['memory_utilization']}"
        self.end_date = datetime.now(tz=UTC)
        self.start_date = self.end_date - timedelta(hours=1)
        self.steps = 60


class PrometheusLoader:
    def __init__(self, host: str):
        self.host = host
        self.query = Query()

    def _fetch_data(self):  # pragma: no cover
        url = f"{self.host}/api/v1/query_range"
        params = {
            "query": self.query.query,
            "start": self.query.start_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "end": self.query.end_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "step": f"{self.query.steps}s",
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def load(self) -> Instances:
        data = self._fetch_data()
        per_instance = group_by_instance_and_date(data)
        return convert_to_metrics(per_instance, duration=self.query.steps)


def group_by_instance_and_date(data: dict) -> dict:
    instances = {}
    for result in data["data"]["result"]:
        instance = result["metric"]["instance"].split(":")[0].lower()
        metric = result["metric"]["metric"].lower()
        if instance not in instances:
            instances[instance] = {}
        for value in result["values"]:
            ts = value[0]
            v = float(value[1])
            if ts not in instances[instance]:
                instances[instance][ts] = {}
            instances[instance][ts][metric] = v
    return instances


def convert_to_metrics(data: dict, duration: int) -> Dict[str, Metrics]:
    instances = {}
    for instance in data:
        metrics = Metrics(data=[])
        for ts in data[instance]:
            dt = datetime.fromtimestamp(ts)
            m = Metric(timestamp=dt, duration=duration)
            for metric in data[instance][ts]:
                value = float(data[instance][ts][metric])
                setattr(m, metric, value)
            metrics.data.append(m)
        instances[instance] = metrics
    return instances
