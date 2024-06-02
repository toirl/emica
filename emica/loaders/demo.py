from datetime import UTC, datetime, timedelta

from emica.core.metrics import Metric, Metrics


class DemoLoader:
    def load(self) -> Metrics:
        metric = Metric(
            timestamp=datetime.now(tz=UTC),
            duration=60,
            cpu_thermal_design_power=20,
            device_emission_embodied=147000,
            device_expected_lifespan=94608000,  # 3 years in seconds
            grid_carbon_intesity=500,  # gCO2/kWh according to Umweltbundesamt in 2022 for Germany
            funtional_unit="duration",
            funtional_unit_time=timedelta(minutes=1),
            cpu_utilization=8.791666666665066,
            memory_utilization=26.267051696777344,
            memory_capacity=16,
        )
        return Metrics(data=[metric])
