from datetime import UTC, datetime

import pytest

from emica.core.metrics import Metric, Metrics
from emica.filters.sci_operation import SCIOperation


def test_fail_on_missing_carbon_grit_attr():
    # Arrange
    m = Metrics(data=[Metric(timestamp=datetime.now(tz=UTC), duration=60)])
    f = SCIOperation()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(m)


def test_fail_on_missing_energy_attr():
    # Arrange
    m = Metrics(data=[Metric(timestamp=datetime.now(tz=UTC), duration=60)])
    f = SCIOperation()
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
                energy=0.00023,
                grid_carbon_intesity=500,
            )
        ]
    )
    # Act
    f = SCIOperation()
    r = f.process(m)
    # Assert
    assert r.data[0].carbon_operational == 0.115
