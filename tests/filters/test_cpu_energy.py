from datetime import UTC, datetime

import pytest

from emica.core.metrics import Metric
from emica.filters.cpu_energy import CPU2Energy, InterpolationMode


def test_process_spline():
    # Arrange
    m = Metric(
        timestamp=datetime.now(tz=UTC), duration=60, cpu_thermal_design_power=20, cpu_utilization=8.791666666665066
    )
    f = CPU2Energy(interpolation=InterpolationMode.SPLINE)
    # Act
    m = f.process(m)
    # Assert
    assert m.cpu_energy == 9.944942598030365e-05


def test_process_linear():
    # Arrange
    m = Metric(
        timestamp=datetime.now(tz=UTC), duration=60, cpu_thermal_design_power=20, cpu_utilization=8.791666666665066
    )
    f = CPU2Energy(interpolation=InterpolationMode.LINEAR)
    # Act
    m = f.process(m)
    # Assert
    assert m.cpu_energy == 9.861111111110043e-05


@pytest.mark.parametrize("attr", ["cpu_thermal_design_power", "cpu_utilization"])
def test_fail_on_missing_attr(attr: str):
    # Arrange
    m = Metric(
        timestamp=datetime.now(tz=UTC), duration=60, cpu_thermal_design_power=20, cpu_utilization=8.791666666665066
    )
    setattr(m, attr, None)
    f = CPU2Energy()
    # Act
    with pytest.raises(ValueError):
        f.process(m)
