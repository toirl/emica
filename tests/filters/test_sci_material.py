from datetime import UTC, datetime

import pytest

from emica.core.metrics import Metric
from emica.filters.sci_material import SCIMaterial


@pytest.mark.parametrize("attr", ["device_emission_embodied", "device_expected_lifespan"])
def test_fail_on_missing_attr(attr: str):
    # Arrange
    m = Metric(
        timestamp=datetime.now(tz=UTC),
        duration=60,
        device_emission_embodied=147000,
        device_expected_lifespan=94608000,  # three years
    )
    setattr(m, attr, None)
    f = SCIMaterial()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(m)


def test_process():
    # Arrange
    m = Metric(
        timestamp=datetime.now(tz=UTC),
        duration=60,
        device_emission_embodied=147000,
        device_expected_lifespan=94608000,  # three years
    )
    # Act
    f = SCIMaterial()
    r = f.process(m)
    # Assert
    assert r.carbon_embodied == 0.09322678843226789
