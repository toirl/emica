from emica.core.pipeline import Pipeline
from emica.filters.cpu_energy import CPU2Energy
from emica.filters.memory_energy import Memory2Energy
from emica.filters.sci import SCI
from emica.filters.sci_energy import SCIEnergy
from emica.filters.sci_material import SCIMaterial
from emica.filters.sci_operation import SCIOperation
from emica.loaders.demo import DemoLoader
from emica.writers.demo import DemoWriter


def test_pipeline():
    # Arrange
    loader = DemoLoader()
    cpu_energy = CPU2Energy()
    memory_energy = Memory2Energy()
    sci_e = SCIEnergy()
    sci_o = SCIOperation()
    sci_m = SCIMaterial()
    sci = SCI()
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
    output_data = pipeline.process(input_data)
    writer.write(output_data)
    # Assert

    expected = output_data.data[0]
    assert expected.sci == 0.0169360230585747
