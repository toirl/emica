from datetime import UTC, datetime

from emica.core.metrics import Instances, Metric, Metrics


class DemoLoader:
    def load(self) -> Instances:
        metric = Metric(
            timestamp=datetime.now(tz=UTC),
            duration=60,
            cpu_utilization=8.791666666665066,
            memory_utilization=26.267051696777344,
            memory_capacity=16,
        )
        return {"demo": Metrics(data=[metric])}
