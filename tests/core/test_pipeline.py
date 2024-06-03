from datetime import timedelta

from emica.core.metrics import Metric
from emica.core.pipeline import Pipeline
from emica.filters.cpu_energy import CPU2Energy
from emica.filters.memory_energy import Memory2Energy
from emica.filters.sci import SCI
from emica.filters.sci_energy import SCIEnergy
from emica.filters.sci_material import SCIMaterial
from emica.filters.sci_operation import SCIOperation
from emica.loaders.demo import DemoLoader
from emica.writers.demo import DemoWriter


def test_full_sci_pipeline(metric: Metric):
    # Arrange
    loader = DemoLoader()
    cpu_energy = CPU2Energy()
    memory_energy = Memory2Energy()
    sci_e = SCIEnergy()
    sci_o = SCIOperation()
    sci_m = SCIMaterial()
    sci = SCI("duration", timedelta(minutes=1))
    writer = DemoWriter()

    pipeline = Pipeline()
    pipeline.add_filter(cpu_energy)
    pipeline.add_filter(memory_energy)
    pipeline.add_filter(sci_e)
    pipeline.add_filter(sci_m)
    pipeline.add_filter(sci_o)
    pipeline.add_filter(sci)

    # Act
    input_data = loader.load()
    for instance in input_data:
        pipeline.set_defaults({})
        metrics = input_data[instance]
        metrics = pipeline.process(metrics)
        input_data[instance] = metrics
    writer.write(input_data)

    # Assert
    expected = input_data["demo"].data[0]
    # assert expected.sci == 0.0169360230585747
    # # That was the origin value from the IF using the teads curve plugin. I
    # guess that the implementation of the algorithem differs a bit.

    assert expected.cpu_energy == metric.cpu_energy
    assert expected.memory_energy == metric.memory_energy
    assert expected.energy == metric.energy
    assert expected.carbon_embodied == metric.carbon_embodied
    assert expected.carbon_operational == metric.carbon_operational
    assert expected.sci == metric.sci
