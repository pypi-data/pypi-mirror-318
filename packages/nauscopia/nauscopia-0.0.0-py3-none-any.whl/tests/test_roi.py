from click.testing import CliRunner

from nauscopia.api.cli import cli
from nauscopia.roi.detect.yolo import YoloDetector


def test_roi_yolo_void(standard_void_png_file, tmp_path, caplog):
    """
    Validate object detection on a bitmap image bearing just void / no objects of interest.
    """

    # Define source/target addresses.
    source = standard_void_png_file
    target = tmp_path / "annotated.mp4"

    # Run detector.
    detector = YoloDetector(input=source, output=target)
    detector.process()

    # Verify outcome.
    assert target.exists(), f"Output file does not exist: {target}"
    assert "Discovered detections: 0" in caplog.messages


def test_roi_yolo_boat_horizon_api_video(standard_boat_horizon_png_file, tmp_path, caplog):
    """
    Validate object detection on a bitmap image with a medium-sized boat on the horizon.
    Output type: Video.
    """

    # Define source/target addresses.
    source = standard_boat_horizon_png_file
    target = tmp_path / "annotated.mp4"

    # Run detector.
    detector = YoloDetector(input=source, output=target)
    detector.process()

    # Verify outcome.
    assert target.exists(), f"Output file does not exist: {target}"
    assert "Discovered detections: 1" in caplog.messages


def test_roi_yolo_boat_horizon_api_bitmap(standard_boat_horizon_png_file, tmp_path, caplog):
    """
    Validate object detection on a bitmap image with a medium-sized boat on the horizon.
    Output type: Bitmap.
    """
    # Define source/target addresses.
    source = standard_boat_horizon_png_file
    target_pattern = tmp_path / "annotated_%03d.png"
    target_effective = tmp_path / "annotated_000.png"

    # Run detector.
    detector = YoloDetector(input=source, output=target_pattern)
    detector.process()

    # Verify outcome.
    assert target_effective.exists(), f"Output file does not exist: {target_effective}"
    assert "Discovered detections: 1" in caplog.messages


def test_roi_yolo_boat_horizon_cli(standard_boat_horizon_png_file, tmp_path, caplog):
    """
    CLI test: Validate object detection on a bitmap image.
    """

    # Define source/target addresses.
    source = standard_boat_horizon_png_file
    target = tmp_path / "annotated.mp4"

    # Run command.
    runner = CliRunner()
    result = runner.invoke(
        cli,
        args=f"--debug detect --input={source} --output={target}",
        catch_exceptions=False,
    )

    # Verify outcome.
    assert result.exit_code == 0
    assert target.exists(), f"Output file does not exist: {target}"
    assert "Discovered detections: 1" in caplog.messages
