import click

from nauscopia.cmd.install import cli as install_cli
from nauscopia.roi.detect.cli import cli as detect_cli
from nauscopia.util.cli import boot_click


@click.group()
@click.option("--verbose", is_flag=True, required=False, help="Turn on logging")
@click.option("--debug", is_flag=True, required=False, help="Turn on logging with debug level")
@click.version_option()
@click.pass_context
def cli(ctx: click.Context, verbose: bool, debug: bool):
    return boot_click(ctx, verbose, debug)


cli.add_command(detect_cli, name="detect")
cli.add_command(install_cli, name="install")
