from datetime import UTC, datetime


class DemoLoader:
    def load(self) -> dict:
        return {
            "timestamp": datetime.now(tz=UTC).isoformat(),
            "duration": 60,
            "cpu/utilization": 10.3,
            "cpu/thermal-design-power": 40,
            "memory/utilization": 34.3,
            "memory/capacity": 16,
        }
