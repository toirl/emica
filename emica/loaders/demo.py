from datetime import UTC, datetime, timedelta

from emica.core.metrics import Metric, Metrics


class DemoLoader:
    def load(self) -> Metrics:
        metric = Metric(
            timestamp=datetime.now(tz=UTC),
            duration=60,
            cpu_thermal_design_power=20,
            device_emission_embodied=167000,
            device_expected_lifespan=94608000,  # 3 years in seconds
            grid_carbon_intesity=434,  # gCO2/kWh according to Umweltbundesamt in 2022 for Germany
            funtional_unit="duration",
            funtional_unit_time=timedelta(minutes=1),
            cpu_utilization=10.3,
            memory_utilization=34.3,
            memory_capacity=16,
        )
        return Metrics(data=[metric])
