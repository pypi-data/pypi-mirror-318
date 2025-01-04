import logging
import time
from pathlib import Path
from typing import Optional, Union

import cv2
from yolov10 import YOLOv10, draw_detections
from yolov10.utils import class_names

from nauscopia.model import DetectionEvent, DetectionLocation
from nauscopia.setting import model_cache_path

logger = logging.getLogger()


class YOLOv10NoPrint(YOLOv10):
    """
    Converge stray `print` statement in YOLOv10 library into `logger.debug()`.
    FIXME: Fix the original code that includes the stray `print` statement.
    """

    def inference(self, input_tensor):
        start = time.perf_counter()
        outputs = self.session.run(self.output_names, {self.input_names[0]: input_tensor})

        logger.debug(f"Inference time: {(time.perf_counter() - start) * 1000:.2f} ms")
        return outputs


class YoloDetector:
    """
    A basic object detector based on YOLOv10.

    Source: https://gitlab.com/sar-eye/HorizonScanner/-/issues/89

    A reference to input media is required. On the output side, either
    provide output media path/url per `--output=` option, and/or toggle
    `--live` view.
    """

    # ONNX model file name.
    MODEL_FILENAME = "yolov10m.onnx"

    # Window name for live view mode.
    LIVEVIEW_WINDOW_NAME = "SARCAM Detector"

    # Output codec.
    # TODO: Make output codec configurable.
    # Possible values: DIVX, H264, mp4v, avc1, XVID, I420
    # http://arahna.de/opencv-save-video/
    OUTPUT_CODEC = "DIVX"  # MPEG-4 codec

    def __init__(
        self,
        input: Optional[Union[str, Path]] = None,
        output: Optional[Union[str, Path]] = None,
        fps: float = 5.0,
        live: bool = False,
    ):
        self.input = input
        self.output = Path(output) if output else None
        self.fps = fps
        self.live = live
        self.detector: YOLOv10

        self.source: cv2.VideoCapture
        self.sink: cv2.VideoWriter

        self.current_frame = 0
        self.detections = 0
        self.setup()

    def make_writer(self):
        """
        Factory for an OpenCV video writer based on input parameters.
        """
        width = int(self.source.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.source.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if self.output_is_bitmap:
            return cv2.VideoWriter(
                filename=str(self.output),
                fourcc=0,
                fps=0,
                frameSize=(width, height),
            )
        else:
            return cv2.VideoWriter(
                filename=str(self.output),
                fourcc=cv2.VideoWriter_fourcc(*self.OUTPUT_CODEC),
                fps=self.fps,
                frameSize=(width, height),
            )

    def setup(self):
        """
        Initialize object detector model.
        """
        model_cache_path.mkdir(parents=True, exist_ok=True)
        model_path = str(model_cache_path / self.MODEL_FILENAME)
        self.detector = YOLOv10NoPrint(model_path, conf_thres=0.2)

    def start(self):
        """
        Start pipeline.
        """
        self.source = cv2.VideoCapture(filename=str(self.input))
        self.sink = self.make_writer()

    def process(self):
        """
        Read data from video source, detect objects, and emit an annotated image and metadata.
        """
        self.start()
        logger.info(f"Reading data from {self.input} with {self.fps} fps")
        if self.output:
            logger.info(f"Writing data to: {self.output}")
        if self.live:
            logger.info("Writing data to workstation live view")
            cv2.namedWindow(self.LIVEVIEW_WINDOW_NAME, cv2.WINDOW_NORMAL)

        logger.info("Press 'q' or escape key to quit.")
        while self.source.isOpened():
            if self.read() is False:
                break
            self.current_frame += 1
        self.source.release()
        self.sink.release()

        logger.info(f"Discovered detections: {self.detections}")
        # cv2.destroyAllWindows()

    def read(self):
        """
        Read data source data and apply object detection.
        """
        # Read from video source, frame by frame.
        success, frame = self.source.read()
        if not success:
            return False

        # Detect objects.
        class_ids, boxes, confidences = self.detector(frame)

        # When detection occurred, write it to the log.
        detections = self.detections_metadata(class_ids, boxes, confidences)
        if detections:
            self.detections += len(detections)
            logger.info(f"Detections: {detections}")

        # Produce image frame annotated with bounding boxes.
        annotated_frame = draw_detections(frame, boxes, confidences, class_ids)

        # Write frame to video sink.
        self.sink.write(annotated_frame)

        # Optionally write to live view.
        if self.live:
            cv2.imshow(self.LIVEVIEW_WINDOW_NAME, annotated_frame)

        # Press key q to stop.
        key = cv2.waitKey(1)
        if key & 0xFF == ord("q"):
            return False

        # Press escape key to stop.
        if key == 27:
            return False

        return True

    def detections_metadata(self, class_ids, boxes, scores):
        """
        A trimmed-down version of `draw_detections`, to gather metadata.
        """
        detections = []
        for class_id, box, confidence in zip(class_ids, boxes, scores):
            label = class_names[class_id]
            detections.append(
                DetectionEvent(
                    label=label,
                    confidence=confidence,
                    location=DetectionLocation(file=self.input, frame=self.current_frame, box=box),
                )
            )

        return detections

    @property
    def output_is_bitmap(self):
        """
        Whether the user wants bitmap(s) instead of a video as output.

        TODO: How to cover the complete list of bitmap image formats
              without needing to enumerate them manually?
        """
        return self.output and self.output.suffix in [
            ".png",
            ".jpg",
            ".jpeg",
            ".tif",
            ".tiff",
            ".bmp",
        ]


def main():
    """
    Run object detection using YOLOv10.
    """
    filename = "/home/sarcam/Videos/sar-recordings/R10/SARCAM-20240201-122520.mp4"
    detector = YoloDetector(filename)
    detector.process()


if __name__ == "__main__":
    main()
