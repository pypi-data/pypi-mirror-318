import logging
import time

import cv2
import numpy as np

logger = logging.getLogger()


def draw_horizon(img, vx, vy, x, y, color, thickness=3):
    m = vy / vx
    t = y - m * x
    if m < 0:
        m = np.clip(m, -1000000000000, -0.000001)
    if m > 0:
        m = np.clip(m, 1000000000000, 0.000001)
    if m == 0:
        m = 0.000001
    pt0 = (int((0 - t) / m), 0)
    pt1 = (int((img.shape[1] - t) / m), img.shape[1])
    img = cv2.line(img, pt0, pt1, color, thickness)
    return img


def draw_hist_cv2(image, log=True):
    h = np.zeros((300, 256, 1))
    bins = np.arange(256).reshape(256, 1)
    hist_item = cv2.calcHist([image], [0], None, [256], [0, 255])
    cv2.normalize(hist_item, hist_item, 0, 255, cv2.NORM_MINMAX)
    if log:
        hist = np.int32(np.log(np.around(hist_item)) * 50)
    else:
        hist = np.int32(np.around(hist_item))
    pts = np.column_stack((bins, hist))
    cv2.polylines(h, [pts], False, 1)
    h = np.flipud(h)
    return h


class DetectorBase:
    """
    Abstract definition of a horizon detector
    """

    def __init__(self, params):
        self._params = params

    def get_horizon(self, image):
        """
        :returns: line_slope_x, line_slope_y, x, y, confidence
        """
        raise NotImplementedError


class RoiCombinedHorizon(DetectorBase):
    """
    Fast horizon detection in maritime images using region-of-interest
    https://journals.sagepub.com/doi/full/10.1177/1550147718790753

    Weak scenes:
    - High reflectance in general
    - If half of image is highly reflecting other half not
    - Low light conditions
    - Very cloudy
    """

    def __init__(self, params):
        super().__init__(params)
        self.invalid_horizon = (-1, -1, -1, -1, -1)

    def detect_roi(self, img=None):
        raise NotImplementedError("detect_roi not implemented yet")

    def get_horizon(self, image):
        start = time.time()
        if self._params["horiz_det_use_roi_det"]:
            start = time.time()
            ROI = self.detect_roi(image)
            image = image[ROI[0] : ROI[1], ROI[2] : ROI[3]]
            end = time.time()
            if self._params["horiz_det_profile"]:
                logger.info("ROI det: %s", end - start)

        vx, vy, x, y, confidence = self.detect_horizon(image)

        if self._params["horiz_det_use_roi_det"]:  # in case ROI is used, correct y coord
            y = y + ROI[0]

        confidence = 1  # TODO find metric
        end = time.time()
        if self._params["horiz_det_profile"]:
            logger.info("horizont: %s", end - start)

        return vx, vy, x, y, confidence

    def remove_outlier(self, image, percentile):
        # Calculate the low and high percentiles
        p_low, p_high = np.percentile(image, [percentile, 100 - percentile])

        # Calculate the mean intensity value of the image
        mean_val = int(image.mean())

        # Replace pixel values outside the low and high percentile range with the mean value
        image_cleaned = image.copy()
        image_cleaned[image_cleaned < p_low] = mean_val
        image_cleaned[image_cleaned > p_high] = mean_val
        return image_cleaned

    def detect_horizon(self, image):
        if self._params["horiz_det_profile"]:
            logger.info("#############")

        start = time.time()
        # first rescale
        scale = self._params["horiz_det_scale_factor"]
        if scale == 0.5:
            interpolation = cv2.INTER_LINEAR
        else:
            interpolation = cv2.INTER_NEAREST
        image = cv2.resize(image, (0, 0), fx=scale, fy=scale, interpolation=interpolation)

        # then rgb -> gray (faster than other way around)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # remove outliers in given percentile before min max normalization
        gray = self.remove_outlier(gray, 0.5)
        if self._params["debug"]:
            cv2.imshow("hist", draw_hist_cv2(gray))

        # normalize image to increase dynamic range for edge detection
        gray = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
        if self._params["debug"]:
            cv2.imshow("norm", gray)

        end = time.time()
        if self._params["horiz_det_profile"]:
            logger.info("preproc: %s", end - start)

        # multiscale edge processing
        start = time.time()
        edgeimage = np.zeros_like(gray)
        medianscales = [31, 61, 81]
        # if self._params['debug']:
        #    for i in medianscales:
        #        cv2.imshow('blur'+str(i), cv2.medianBlur(gray,i))

        weight = np.float32(1.0 / (len(medianscales)))
        cannyMin = self._params["horiz_det_canny_min"]  # below will not be considered as edge
        # between will be considered as edge, if connected to strong edge
        cannyMax = self._params["horiz_det_canny_max"]  # above will be considered as strong edge
        for oneMedianScale in medianscales:
            if oneMedianScale < 1:
                median = gray
            else:
                median = cv2.medianBlur(gray, oneMedianScale)  # takes longest in profiler
            canny = cv2.Canny(median, cannyMin, cannyMax) * weight
            edgeimage = cv2.add(edgeimage, canny.astype(np.uint8))
        end = time.time()
        if self._params["horiz_det_profile"]:
            logger.info("canny: %s", end - start)

        if self._params["debug"]:
            cv2.imshow("edgeimage", edgeimage)

        if np.max(edgeimage) == 0:
            if self._params["debug"]:
                logger.info(f"{str(time.time())}:edgeimage max == 0")
            cv2.waitKey(1)
            return self.invalid_horizon

        # Only keep strongest edges
        edges_threshold = self._params["horiz_det_edge_threshold"]
        ret, threshed = cv2.threshold(edgeimage, edges_threshold, 255, cv2.THRESH_BINARY)

        if self._params["debug"]:
            cv2.imshow("threshed", threshed)

        if np.max(threshed) == 0:
            if self._params["debug"]:
                logger.info(f"{str(time.time())}:threshed max == 0")
            cv2.waitKey(1)
            return self.invalid_horizon

        # Inital horizont guess via hough transform
        houghThresh = threshed.shape[0] // 8
        houghAngularRes = np.deg2rad(0.5)
        houghMaxAngleHorizon = 30

        # Probabilistic approach is not as accurate and fast
        # as normal hough, due to angle min max @ normal.
        start = time.time()
        lines = cv2.HoughLines(
            image=threshed,
            rho=1,
            theta=houghAngularRes,
            threshold=houghThresh,
            min_theta=np.deg2rad(90 - houghMaxAngleHorizon),
            max_theta=np.deg2rad(90 + houghMaxAngleHorizon),
        )

        if lines is None:
            if self._params["debug"]:
                logger.debug(f"{str(time.time())}:lines == 0")
            cv2.waitKey(1)
            return self.invalid_horizon

        for rho, theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
        end = time.time()
        if self._params["horiz_det_profile"]:
            logger.info("hough: %s", end - start)

        # calc residual / error of every pixel in edge image to hough line
        start = time.time()
        x1, y1, x2, y2 in lines[0]  # get line description by using the two points of the hough line
        denom = np.sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1))
        thresholdedNonZero = cv2.findNonZero(threshed)
        x3 = thresholdedNonZero[:, :, 0]
        y3 = thresholdedNonZero[:, :, 1]
        residuals = abs((y2 - y1) * x3 - (x2 - x1) * y3 + x2 * y1 - y2 * x1) / denom
        residuals = residuals.reshape(len(thresholdedNonZero))
        end = time.time()
        if self._params["horiz_det_profile"]:
            logger.info("residuals: %s", end - start)

        # median filter thresholded pixels by residual / error => only keep pts with low error
        start = time.time()
        q1 = np.quantile(
            residuals, self._params["horiz_det_thresholded_q1"]
        )  # calc q1 quantile for filtering
        q1FilteredHorizontPts = thresholdedNonZero[residuals < q1]
        end = time.time()
        if self._params["horiz_det_profile"]:
            logger.info("medianfilter: %s", end - start)

        # fit final horizontal line by calc line through median filted points
        start = time.time()
        [vx, vy, x, y] = cv2.fitLine(
            points=q1FilteredHorizontPts, distType=cv2.DIST_L1, param=0, reps=0.01, aeps=0.01
        )
        end = time.time()
        if self._params["horiz_det_profile"]:
            logger.info("fitline: %s", end - start)

        if self._params["debug"]:
            cv2.imshow("result", draw_horizon(image, vx, vy, x, y, (0, 0, 255)))
            cv2.waitKey(1)

        # move line to image center
        m = vy / vx
        t = y - m * x
        xnew = image.shape[1] / 2
        ynew = m * xnew + t
        x = xnew
        y = ynew

        # scale horizon according to image scaling factor
        x = x * 1.0 / scale
        y = y * 1.0 / scale

        confidence = (
            1  # TODO: use error of points to fitted horizon line as a indicator for confidence
        )

        # convert values
        vx = float(vx)
        vy = float(vy)
        x = float(x)
        y = float(y)
        confidence = float(confidence)

        return vx, vy, x, y, confidence


class KMeanHorizon(DetectorBase):
    def __init__(self, params):
        super().__init__(params)

    def get_horizon(self, image):
        # Load params
        k_mean_stepsize = self._params["k_mean_stepsize"]
        k_mean_width = self._params["k_mean_width"]

        # Make gray image
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Binary image in which the horizon points are placed
        points = np.zeros_like(gray_image)

        # Iterate over vertical image slices
        for i in range(0, int(image.shape[1] - k_mean_width), k_mean_stepsize):
            # Get vertical image slice as float array
            Z = np.float32(cv2.cvtColor(image[:, i : i + k_mean_width], cv2.COLOR_BGR2HSV))

            Z = np.mean(Z, axis=1)

            # K-Means termination settings
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            # Number of classes
            K = 2
            # K-Means calculation
            ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

            # Determine which class is the sky
            if label[0] != 1:
                # Invert if the sky is not class 1
                label = np.invert(label)

            # Weired bug fix
            if int(np.count_nonzero((label))) == 400:
                continue

            # Determine how many sky pixels are in the slice and
            # approximate them as the y coordinate.
            point = (i, int(np.count_nonzero((label))))

            # Draw horizon point in map
            cv2.circle(points, point, 1, 255, -1)  # TODO  use list of points instead

        # Fit a RANSEC like line in the horizon point map  (default params)
        [line_slope_x, line_slope_y, line_base_x, line_base_y] = cv2.fitLine(
            np.argwhere(points == 255), cv2.DIST_L1, 0, 0.005, 0.01
        )

        confidence = 1  # TODO find better confidence metric

        """
        alpha = 1.0
        beta = 1.0 - alpha
        gray_image = cv2.addWeighted(points, 1, gray_image, 1, 0)
        cv2.imshow("a", gray_image)
        """

        return line_slope_y, -line_slope_x, line_base_y, line_base_x, confidence
