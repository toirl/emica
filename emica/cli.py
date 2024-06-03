"""Console script for emica"""

import sys

import click

from emica.logger import get_logger, setup_logging
from emica.main import main

logger = get_logger()


@click.command()
@click.option("-c", "--config", help="Path to config file", required=True)
@click.option("-v", "--verbosity", default=0, count=True, help="Verbosity of logging")
def cli_main(verbosity: int, config: str, args=None):
    """Console script for emica"""
    setup_logging(verbosity=verbosity)
    return main(verbosity, config)


if __name__ == "__main__":
    sys.exit(cli_main())  # pragma: no cover
