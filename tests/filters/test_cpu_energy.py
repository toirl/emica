from datetime import UTC, datetime

import pytest

from emica.core.metrics import Metric
from emica.filters.cpu_energy import CPU2Energy


def test_process():
    # Arrange
    m = Metric(
        timestamp=datetime.now(tz=UTC), duration=60, cpu_thermal_design_power=20, cpu_utilization=8.791666666665066
    )
    f = CPU2Energy()
    # Act
    m = f.process(m)
    # Assert
    assert m.cpu_energy == 0.00019839970774255318


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
