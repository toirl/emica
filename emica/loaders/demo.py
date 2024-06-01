from datetime import UTC, datetime

from emica.core.metrics import Metric, Metrics


class DemoLoader:
    def load(self) -> Metrics:
        metric = Metric(
            timestamp=datetime.now(tz=UTC),
            cpu_utilization=10.3,
            duration=60,
            cpu_thermal_design_power=40,
            memory_utilization=34.3,
            memory_capacity=16,
        )
        return Metrics(data=[metric])
