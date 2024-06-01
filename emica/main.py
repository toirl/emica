from emica.core.pipeline import Pipeline
from emica.filters.demo import DemoFilter
from emica.loaders.demo import DemoLoader
from emica.logger import setup_logging
from emica.writers.demo import DemoWriter


def main():
    setup_logging(verbosity=5)
    loader = DemoLoader()
    input_data = loader.load()
    filter = DemoFilter()
    pipeline = Pipeline()
    pipeline.add_filter(filter)
    output_data = pipeline.process(input_data)
    writer = DemoWriter()
    writer.write(output_data)


if __name__ == "__main__":
    main()
