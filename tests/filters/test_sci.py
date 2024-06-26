from datetime import timedelta

import pytest

from emica.core.metrics import Metric
from emica.filters.sci import SCI


def test_process(metric: Metric):
    # Arrange
    f = SCI("duration", timedelta(minutes=1))
    # Act
    r = f.process(metric)
    # Assert
    assert r.sci == 0.016111437377222617


@pytest.mark.parametrize("attr", ["carbon_operational,carbon_embodied"])
def test_fail_on_missing_attr(attr: str, metric: Metric):
    # Arrange
    for a in attr.split(","):
        setattr(metric, a, None)
    f = SCI("duration", timedelta(minutes=1))
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(metric)
