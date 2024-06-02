from datetime import UTC, datetime

import pytest

from emica.core.metrics import Metric
from emica.filters.sci_energy import SCIEnergy


@pytest.mark.parametrize("attr", ["memory_energy,cpu_energy"])
def test_fail_on_missing_attr(attr: str):
    # Arrange
    m = Metric(
        timestamp=datetime.now(tz=UTC),
        duration=60,
        memory_energy=0.001872,
        cpu_energy=0.00231,
    )
    for a in attr.split(","):
        setattr(m, a, None)
    f = SCIEnergy()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(m)


def test_process():
    # Arrange
    m = Metric(
        timestamp=datetime.now(tz=UTC),
        duration=60,
        memory_energy=0.001872,
        cpu_energy=0.00231,
    )
    f = SCIEnergy()
    # Act
    r = f.process(m)
    # Assert
    assert r.energy == 0.004182
