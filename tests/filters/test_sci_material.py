import pytest

from emica.core.metrics import Metric
from emica.filters.sci_material import SCIMaterial


@pytest.mark.parametrize("attr", ["device_emission_embodied", "device_expected_lifespan"])
def test_fail_on_missing_attr(attr: str, metric: Metric):
    # Arrange
    setattr(metric, attr, None)
    f = SCIMaterial()
    # Act
    # Assert
    with pytest.raises(ValueError):
        f.process(metric)


def test_process(metric: Metric):
    # Arrange
    # Act
    f = SCIMaterial()
    r = f.process(metric)
    # Assert
    assert r.carbon_embodied == 0.09322678843226789
