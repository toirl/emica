from datetime import UTC, datetime

import pytest

from emica.core.metrics import Metric, Metrics
from emica.filters.sci_material import SCIMaterial


def test_fail_on_missing_emission_embodied_attr():
    # Arrange
    m = Metrics(data=[Metric(timestamp=datetime.now(tz=UTC), duration=60)])
    f = SCIMaterial()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(m)


def test_fail_on_missing_expected_lifespan():
    # Arrange
    m = Metrics(data=[Metric(timestamp=datetime.now(tz=UTC), duration=60)])
    f = SCIMaterial()
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
                device_emission_embodied=1234,
                device_expected_lifespan=94608000,  # three years
            )
        ]
    )
    # Act
    f = SCIMaterial()
    r = f.process(m)
    # Assert
    assert r.data[0].carbon_embodied == 0.00078259766615931
