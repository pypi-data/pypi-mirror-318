import logging
import os
import sys

import cv2
import numpy as np
import yaml

from nauscopia.horizon.algorithm import RoiCombinedHorizon
from nauscopia.horizon.stabilizer import rotate_and_center_horizon

logger = logging.getLogger()


class HorizonDetector:
    def __init__(self, config):
        self._horizon_detector = RoiCombinedHorizon(config)

        self._debug = config["debug"]

        self.config = config

        # Placeholders
        self._last_frame_feature_map = None

    def analyse_image(self, image, stamp):  # noqa: ARG002
        # Get the horizon in the image
        line_slope_x, line_slope_y, line_base_x, line_base_y, _ = (
            self._horizon_detector.get_horizon(image)
        )

        if line_base_x == -1:  # invalid horizon
            return (0, 0, 0, 0, False)

        horizon = (line_slope_x, line_slope_y, line_base_x, line_base_y, True)

        return horizon

    def horizon_to_image_center_angular_delta(self, horizon, imageshape, camModel):
        # calculate pitch and roll angles of horizon in image using the camera calibration

        ## pitch
        # calculate vector to imagecenter point
        Point2DImgCenter = np.array([imageshape[1] / 2, imageshape[0] / 2], int)
        Point3DImgCenterCamCoord = camModel.projectPixelTo3dRay(
            Point2DImgCenter
        )  # project image coords to sensor coords
        Point3DImgCenterCamCoordZYplane = np.array(
            [Point3DImgCenterCamCoord[2], Point3DImgCenterCamCoord[1]]
        )  # use ZY plane to get a 2D Vector
        Point3DImgCenterCamCoordZYplaneUnit = Point3DImgCenterCamCoordZYplane / np.linalg.norm(
            Point3DImgCenterCamCoordZYplane
        )  # norm this vector
        # calculate vector to center horizon point
        Point2DHorizonImg = np.array([int(horizon[2]), int(horizon[3])], int)
        Point3DHorizonCamCoord = camModel.projectPixelTo3dRay(Point2DHorizonImg)
        Point3DHorizonCamCoordZYplane = np.array(
            [Point3DHorizonCamCoord[2], Point3DHorizonCamCoord[1]]
        )
        Point3DHorizonCamCoordZYplaneUnit = Point3DHorizonCamCoordZYplane / np.linalg.norm(
            Point3DHorizonCamCoordZYplane
        )
        # calculate angle between the two unit vectors / points
        pitch = np.rad2deg(
            np.arcsin(
                np.cross(Point3DImgCenterCamCoordZYplaneUnit, Point3DHorizonCamCoordZYplaneUnit)
            )
        )

        ## roll
        # calc roll using horizon slope
        roll = -np.rad2deg(np.arctan(horizon[1] / horizon[0]))

        horizon_angular = (roll, pitch)
        return horizon_angular


if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), "../../../config/config.yaml")

    config_path = os.path.realpath(config_path)

    if not os.path.exists(config_path):
        logger.error(
            "No config file specified, see the 'example.config.yaml' in "
            "'config' and save your version as 'config.yaml'."
        )
        sys.exit(1)

    with open(config_path, "r") as f:
        params = yaml.safe_load(f)

    videoSource = "/home/sarcam/Downloads/VID_20180818_063555.mp4"
    ht = HorizonDetector(params)

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
            horizon = ht.analyse_image(frame, stamp)
            if horizon[4]:
                rotImg = rotate_and_center_horizon(
                    frame, horizon[0], horizon[1], horizon[2], horizon[3]
                )
            else:
                rotImg = frame
            rotImg = cv2.resize(rotImg, (0, 0), fx=0.5, fy=0.5)
            cv2.imshow("rotImg", rotImg)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                pass
            frameNr = frameNr + 1
        # Break the loop
        else:
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()
