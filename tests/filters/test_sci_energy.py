from datetime import UTC, datetime

import pytest

from emica.core.metrics import Metric, Metrics
from emica.filters.sci_energy import SCIEnergy


def test_fail_on_missing_energy_attr():
    # Arrange
    m = Metrics(data=[Metric(timestamp=datetime.now(tz=UTC), duration=60, memory_utilization=30)])
    f = SCIEnergy()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(m)


def test_calculation():
    # Arrange
    m = Metrics(
        data=[
            Metric(
                timestamp=datetime.now(tz=UTC),
                duration=60,
                memory_capacity=16,
                memory_energy=0.001872,
                cpu_energy=0.00231,
            )
        ]
    )
    f = SCIEnergy()
    # Act
    r = f.process(m)
    # Assert
    assert r.data[0].energy == 0.004182
