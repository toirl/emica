from datetime import UTC, datetime

import pytest

from emica.core.config import InstanceConfig
from emica.core.metrics import Metric


@pytest.fixture
def metric() -> Metric:
    m = Metric(
        timestamp=datetime.now(tz=UTC),
        duration=60,
        cpu_thermal_design_power=20,
        cpu_utilization=8.791666666665066,
        memory_capacity=16,
        memory_utilization=26.267051696777344,
        device_emission_embodied=147000,
        device_expected_lifespan=94608000,  # three years
        grid_carbon_intensity=500,
        # Calculated
        memory_energy=0.001647469482421875,
        cpu_energy=9.944942598030365e-05,
        energy=0.0017469189084021786,
        carbon_embodied=0.09322678843226789,
        carbon_operational=0.8734594542010893,
        sci=0.016111437377222617,
    )
    return m


@pytest.fixture
def config() -> InstanceConfig:
    return InstanceConfig("instances.yaml")
