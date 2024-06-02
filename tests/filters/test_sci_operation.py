from datetime import UTC, datetime

import pytest

from emica.core.metrics import Metric
from emica.filters.sci_operation import SCIOperation


@pytest.mark.parametrize("attr", ["energy", "grid_carbon_intesity"])
def test_fail_on_missing_energy_attr(attr: str):
    # Arrange
    m = Metric(
        timestamp=datetime.now(tz=UTC),
        duration=60,
        energy=0.00023,
        grid_carbon_intesity=500,
    )
    setattr(m, attr, None)
    f = SCIOperation()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(m)


def test_calculation():
    # Arrange
    m = Metric(
        timestamp=datetime.now(tz=UTC),
        duration=60,
        energy=0.00023,
        grid_carbon_intesity=500,
    )
    # Act
    f = SCIOperation()
    r = f.process(m)
    # Assert
    assert r.carbon_operational == 0.115
