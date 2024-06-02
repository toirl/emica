from datetime import UTC, datetime

import pytest

from emica.core.metrics import Metric, Metrics
from emica.filters.cpu_energy import CPU2Energy


def test_fail_on_missing_tdp_attr_cpu_energy():
    # Arrange
    m = Metrics(data=[Metric(timestamp=datetime.now(tz=UTC), duration=60, cpu_utilization=10)])
    f = CPU2Energy()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(m)


def test_fail_on_missing_cpu_attr_cpu_energy():
    # Arrange
    m = Metrics(data=[Metric(timestamp=datetime.now(tz=UTC), duration=60, cpu_thermal_design_power=40)])
    f = CPU2Energy()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(m)


def test_cpu_attr_cpu_energy():
    # Arrange
    m = Metrics(
        data=[Metric(timestamp=datetime.now(tz=UTC), duration=60, cpu_thermal_design_power=40, cpu_utilization=10)]
    )
    f = CPU2Energy()
    # Act
    r = f.process(m)
    # Assert
    assert r.data[0].cpu_energy == 4.0
