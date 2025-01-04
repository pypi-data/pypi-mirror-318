import logging

import colorlog
from colorlog.escape_codes import escape_codes


def setup_logging(
    level=logging.INFO,
    verbose: bool = False,  # noqa: ARG001
    debug: bool = False,  # noqa: ARG001
    width: int = 24,
):
    reset = escape_codes["reset"]
    log_format = (
        f"%(asctime)-15s [%(name)-{width}s] %(log_color)s%(levelname)-8s:{reset} %(message)s"
    )

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(log_format))

    logging.basicConfig(format=log_format, level=level, handlers=[handler])
