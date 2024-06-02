from datetime import UTC, datetime, timedelta

import pytest

from emica.core.metrics import Metric, Metrics
from emica.filters.sci import SCI


def test_calculation():
    # Arrange
    m = Metrics(
        data=[
            Metric(
                timestamp=datetime.now(tz=UTC),
                duration=60,
                carbon_embodied=0.00023,
                carbon_operational=0.00023,
                funtional_unit="duration",
                funtional_unit_time=timedelta(minutes=1),
            )
        ]
    )
    # Act
    f = SCI()
    r = f.process(m)
    # Assert
    assert r.data[0].sci == 0.00046


@pytest.mark.parametrize("attr", ["carbon_operational,carbon_embodied", "funtional_unit", "funtional_unit_time"])
def test_fail_on_missing_attr(attr: str):
    # Arrange
    m = Metrics(
        data=[
            Metric(
                timestamp=datetime.now(tz=UTC),
                duration=60,
                carbon_embodied=0.00023,
                carbon_operational=0.00023,
                funtional_unit="duration",
                funtional_unit_time=timedelta(minutes=1),
            )
        ]
    )
    for a in attr.split(","):
        setattr(m.data[0], a, None)
    f = SCI()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(m)
