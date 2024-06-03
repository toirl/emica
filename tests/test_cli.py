#!/usr/bin/env python

"""Tests for `emica` package."""

from click.testing import CliRunner

from emica import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.cli_main)
    assert result.exit_code == 0
    help_result = runner.invoke(cli.cli_main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help           Show this message and exit." in help_result.output
