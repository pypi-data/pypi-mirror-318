import logging

import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage, Image

cv_bridge = CvBridge()


logger = logging.getLogger()


def ros_image_message_to_opencv(rosImgMsg):
    if isinstance(rosImgMsg, CompressedImage):
        np_arr = np.fromstring(rosImgMsg.data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    elif isinstance(rosImgMsg, Image):
        # Get image from message
        frame = cv_bridge.imgmsg_to_cv2(rosImgMsg)  # , 'bgr8')
    else:
        raise TypeError(f"Unknown image type: {type(rosImgMsg)}")
    return frame
