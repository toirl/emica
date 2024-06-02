from datetime import UTC, datetime

import pytest

from emica.core.metrics import Metric, Metrics
from emica.filters.memory_energy import Memory2Energy


def test_fail_on_missing_memcap_attr():
    # Arrange
    m = Metrics(data=[Metric(timestamp=datetime.now(tz=UTC), duration=60, memory_utilization=30)])
    f = Memory2Energy()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(m)


def test_fail_on_missing_memutil_attr():
    # Arrange
    m = Metrics(data=[Metric(timestamp=datetime.now(tz=UTC), duration=60, memory_capacity=16)])
    f = Memory2Energy()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(m)


def test_calculation():
    # Arrange
    m = Metrics(data=[Metric(timestamp=datetime.now(tz=UTC), duration=60, memory_capacity=16, memory_utilization=30)])
    f = Memory2Energy()
    # Act
    r = f.process(m)
    # Assert
    assert r.data[0].memory_energy == 0.001872
