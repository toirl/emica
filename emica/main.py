from datetime import timedelta

from emica.core.config import InstanceConfig
from emica.core.pipeline import Pipeline
from emica.filters.cpu_energy import CPU2Energy
from emica.filters.memory_energy import Memory2Energy
from emica.filters.sci import SCI
from emica.filters.sci_energy import SCIEnergy
from emica.filters.sci_material import SCIMaterial
from emica.filters.sci_operation import SCIOperation
from emica.loaders.demo import DemoLoader
from emica.logger import get_logger, setup_logging
from emica.writers.demo import DemoWriter

log = get_logger()


def main():
    setup_logging(verbosity=5)
    config = InstanceConfig("./instances.yaml")
    loader = DemoLoader()
    #    loader = PrometheusLoader(host="http://localhost:9090")
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
    sci = SCI("duration", timedelta(minutes=1))
    pipeline.add_filter(sci)

    for instance in input_data:
        log.info("Processing Instance", instance=instance)
        defaults = config.get_defaults(instance)
        pipeline.set_defaults(defaults)
        metrics = input_data[instance]
        metrics = pipeline.process(metrics)
        input_data[instance] = metrics

    writer = DemoWriter()
    writer.write(input_data)


if __name__ == "__main__":
    main()
