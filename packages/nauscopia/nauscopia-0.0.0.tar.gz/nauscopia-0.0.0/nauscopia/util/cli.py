import logging

import click

from nauscopia.util.log import setup_logging


def boot_click(
    ctx: click.Context,  # noqa: ARG001
    verbose: bool = False,
    debug: bool = False,
):
    """
    Bootstrap the CLI application.
    """

    # Adjust log level according to `verbose` / `debug` flags.
    log_level = logging.INFO
    if debug:
        log_level = logging.DEBUG

    # Setup logging, according to `verbose` / `debug` flags.
    setup_logging(level=log_level, verbose=verbose, debug=debug)
