import logging
import os

import cv2
import numpy as np
import yaml

from nauscopia.roi.detect.opencv_boat_finder import GradientBoatFinder
from nauscopia.roi.detect.opencv_candidates import CandidateFinder

logger = logging.getLogger()


class BoatDetector:
    def __init__(self, config):
        self._roi_boat_finder = GradientBoatFinder(config)
        self._candidate_finder = CandidateFinder()

        self._debug = config["debug"]

        self.config = config

        # Placeholders
        self._last_frame_feature_map = None
        self._camModel = None

    def analyse_image(self, image, stamp, history=True):  # noqa: ARG002
        # Crop roi out of rotated image => done in image stabilizer
        # horizon_y_pos=image.shape[0] / 2
        # roi = image[
        #    max(
        #        int(horizon_y_pos - self.config['default_roi_height'] // 2),
        #        0)
        #    :
        #    min(
        #        int(horizon_y_pos + self.config['default_roi_height'] // 2),
        #        image.shape[0]),
        #    :]
        roi = image

        # Get feature map
        feature_map = self._roi_boat_finder.find_boats_in_roi(roi)

        # Get K for the complementary filter
        K = self.config["complementary_filter_k"]

        # Calculate time based low pass using the complementary filter
        if history and self._last_frame_feature_map is not None:
            feature_map = (self._last_frame_feature_map * K + feature_map * (1 - K)).astype(
                np.uint8
            )
        elif history:
            # FIXME: Assigned but never used.
            history_map = (feature_map * (1 - K)).astype(np.uint8)  # noqa: F841

        # Add median filter for noise suppression
        median_features = cv2.medianBlur(feature_map, 3)

        # Calculate mean of detections
        mean = np.mean(median_features, axis=1)

        # Add threshold
        _, median_features_thresh = cv2.threshold(
            median_features, int(mean + self.config["threshold"]), 255, cv2.THRESH_BINARY
        )

        # Set last image to current image
        if history:
            self._last_frame_feature_map = feature_map.copy()

        candidates = self._candidate_finder.get_candidates(median_features_thresh)

        if self._debug:
            # Draw candidates
            candidate_canvas = np.zeros_like(roi)
            roi_height = (
                self.config["image_stab_roi_above_horizon"]
                + self.config["image_stab_roi_below_horizon"]
            )
            if candidates:
                candidate_canvas_part = np.zeros((roi_height, 0, 3), dtype=np.uint8)
                for index, candidate in enumerate(candidates):
                    candidate_canvas_part = np.concatenate(
                        (candidate_canvas_part, roi[:, candidate[0] : candidate[1], :]), axis=1
                    )
                    candidate_canvas_part = np.concatenate(
                        (candidate_canvas_part, np.zeros((roi_height, 5, 3), dtype=np.uint8)),
                        axis=1,
                    )
                candidate_canvas[:, : candidate_canvas_part.shape[1] - 5, :] += (
                    candidate_canvas_part[:, :-5, :]
                )

            # Repeat for viz
            feature_map_large = np.repeat(feature_map, 60, axis=0)
            median_features_thresh_large = np.repeat(median_features_thresh, 60, axis=0)
            combines_detections = np.concatenate(
                (feature_map_large, median_features_thresh_large), axis=0
            )
            roi_view = cv2.resize(roi, (combines_detections.shape[1], 60))
            detections_with_roi = np.concatenate(
                (roi_view, cv2.cvtColor(combines_detections, cv2.COLOR_GRAY2BGR)), axis=0
            )
            detections_with_roi = np.concatenate(
                (
                    detections_with_roi,
                    cv2.resize(candidate_canvas, (combines_detections.shape[1], 60)),
                ),
                axis=0,
            )
            # Show images
            cv2.imshow("Detections", detections_with_roi)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                pass

        return (True, roi, median_features, median_features_thresh, candidates)


if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), "../../config/config.yaml")

    config_path = os.path.realpath(config_path)

    if not os.path.exists(config_path):
        logger.error(
            "No config file specified, see the 'example.config.yaml' in "
            "'config' and save your version as 'config.yaml'."
        )

    with open(config_path, "r") as f:
        params = yaml.safe_load(f)

    videoSource = (
        "/home/julle/ControlerProjekte/SAR-Eye/data/boatCam/SchwedenFaehre/VID_20180818_063412.mp4"
    )
    videoSource = "/media/julle/seagate/data/robHorizon/16.01/16.1_2-contam/3trawler.MTS"
    bt = BoatDetector(params)

    cap = cv2.VideoCapture(videoSource)
    # cap.set(cv2.CAP_PROP_POS_FRAMES,500)
    # Read until video is completed
    frameNr = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret is True:
            # Display the resulting frame
            # cv2.imshow('Frame',frame)
            stamp = frameNr * 1 / fps
            bt.analyse_image(frame, stamp)

            frameNr = frameNr + 1
        # Break the loop
        else:
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()
