import click

from nauscopia.roi.detect.yolo import YoloDetector


@click.command()
@click.version_option()
@click.pass_context
def cli(
    ctx: click.Context,  # noqa: ARG001
):
    """
    Install runtime dependencies.
    """

    # Invoke it once to make it download its model.
    YoloDetector()
