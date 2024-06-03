import pytest

from emica.core.metrics import Metric
from emica.filters.sci_energy import SCIEnergy


@pytest.mark.parametrize("attr", ["memory_energy,cpu_energy"])
def test_fail_on_missing_attr(attr: str, metric: Metric):
    # Arrange
    for a in attr.split(","):
        setattr(metric, a, None)
    f = SCIEnergy()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(metric)


def test_process(metric: Metric):
    # Arrange
    f = SCIEnergy()
    # Act
    r = f.process(metric)
    # Assert
    assert r.energy == 0.0017469189084021786
