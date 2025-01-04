import cv2
import numpy as np


def rotate_and_center_horizon(img, vx, vy, x, y, fill_black=False):
    # parse input
    sx = img.shape[1] / 2
    l = (sx - x) / vx  # noqa: E741
    sy = y + l * vy
    horizonCenterPt = (sx, sy)
    angle = np.rad2deg(np.tan(vy / vx))

    # Create transfrom matrix
    M_rotate = cv2.getRotationMatrix2D(horizonCenterPt, angle, 1)
    M_translate2Center = np.zeros((2, 3), float)
    M_translate2Center[0, 2] = (img.shape[1] / 2) - horizonCenterPt[0]
    M_translate2Center[1, 2] = (img.shape[0] / 2) - horizonCenterPt[1]
    M = M_rotate + M_translate2Center

    cols = img.shape[1]
    rows = img.shape[0]

    # Rotate image using affine warp
    # Interpolation: Nearest neighbor for lowest CPU usage
    # TODO: use cuda variant ?
    if fill_black:
        return cv2.warpAffine(img, M, (cols, rows), flags=cv2.INTER_LINEAR)
    else:
        # get mean / average color to avoid black background (fast sampling)
        flat_image = img.reshape(-1, img.shape[-1])
        selected_px = np.random.randint(0, flat_image.shape[0], 1000)
        mean_color = flat_image[selected_px].mean(axis=0)
        return cv2.warpAffine(
            img,
            M,
            (cols, rows),
            flags=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_CONSTANT,
            borderValue=mean_color,
        )


def crop_image_horizon_ROI(img, pixAboveHorizon, pixBelowHorizon):
    horizon_y_pos = img.shape[0] / 2
    img_roi = img[
        max(int(horizon_y_pos - pixAboveHorizon), 0) : min(
            int(horizon_y_pos + pixBelowHorizon), img.shape[0]
        ),
        :,
    ]

    return img_roi


def transform_back_to_unstabilized_detection(croppedImgShape, pt, vx, vy, x, y):  # noqa: ARG001
    pt_homo = np.zeros((3, 1), float)
    pt_homo[0] = pt[0]
    pt_homo[1] = pt[1]
    pt_homo[2] = 1.0

    # rotate back to unstabilized
    horizonCenterPt = (croppedImgShape[0] // 2, croppedImgShape[1] // 2)
    angle = np.rad2deg(np.arctan(vy / vx))
    M_rotateCV2 = cv2.getRotationMatrix2D(horizonCenterPt, angle, 1)
    M_rotate = np.eye(3)
    M_rotate[0:2, 0:3] = M_rotateCV2
    pt_homo = M_rotate @ pt_homo

    # translate back to horizon positon
    pt_homo[0] = pt_homo[0] + y - croppedImgShape[0] // 2

    return np.array([pt_homo[0], pt_homo[1]], int)


if __name__ == "__main__":
    croppedImgShape = [20, 2000]
    pt = [10, 0]
    vx = 1.0
    vy = -1.0
    x = 1000 / 2
    y = 2000 / 2
    pt = transform_back_to_unstabilized_detection(croppedImgShape, pt, vx, vy, x, y)
    print(pt)  # noqa: T201
