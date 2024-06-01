from emica.core.pipeline import Pipeline
from emica.filters.cpu_energy import CPU2Energy
from emica.filters.memory_energy import Memory2Energy
from emica.filters.sci import SCI
from emica.filters.sci_energy import SCIEnergy
from emica.filters.sci_material import SCIMaterial
from emica.filters.sci_operation import SCIOperation
from emica.loaders.demo import DemoLoader
from emica.logger import setup_logging
from emica.writers.demo import DemoWriter


def main():
    setup_logging(verbosity=5)
    loader = DemoLoader()
    input_data = loader.load()

    pipeline = Pipeline()
    cpu_energy = CPU2Energy()
    pipeline.add_filter(cpu_energy)
    memory_energy = Memory2Energy()
    pipeline.add_filter(memory_energy)
    sci_e = SCIEnergy()
    pipeline.add_filter(sci_e)
    sci_m = SCIMaterial()
    pipeline.add_filter(sci_m)
    sci_o = SCIOperation()
    pipeline.add_filter(sci_o)
    sci = SCI()
    pipeline.add_filter(sci)

    output_data = pipeline.process(input_data)
    writer = DemoWriter()
    writer.write(output_data)


if __name__ == "__main__":
    main()
