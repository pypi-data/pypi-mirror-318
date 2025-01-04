import click

from nauscopia.roi.detect.yolo import YoloDetector


@click.command()
@click.option("--input", "-i", "input_", type=str, required=True, help="Input video or image")
@click.option("--output", "-o", type=str, required=False, help="Output video or image")
@click.option(
    "--fps", "-f", type=float, required=False, default=5, help="Frames per second (fps). Default: 5"
)
@click.option("--live", is_flag=True, required=False, help="Turn on live view")
@click.version_option()
@click.pass_context
def cli(
    ctx: click.Context,  # noqa: ARG001
    input_: str,
    output: str,
    fps: float,
    live: bool,
):
    """
    Run object detection via command line interface.
    """
    detector = YoloDetector(input=input_, output=output, fps=fps, live=live)
    detector.process()
