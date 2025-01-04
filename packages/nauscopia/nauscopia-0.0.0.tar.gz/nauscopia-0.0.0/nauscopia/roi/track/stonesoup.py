import copy
import logging

# Kalman tracker
from datetime import datetime
from enum import IntEnum

import cv2
import numpy as np

# Association
from scipy import linalg
from scipy.optimize import linear_sum_assignment
from stonesoup.models.measurement.linear import LinearGaussian
from stonesoup.models.transition.linear import (
    # CombinedLinearGaussianTransitionModel,
    ConstantVelocity,
    # LinearGaussianTransitionModel,
)
from stonesoup.predictor.kalman import KalmanPredictor
from stonesoup.types.detection import Detection as TrackDetection
from stonesoup.types.hypothesis import SingleHypothesis
from stonesoup.types.state import GaussianState
from stonesoup.updater.kalman import KalmanUpdater

logger = logging.getLogger()

NOT_ASSOC = -1
HUGE_COSTS = 99999999999999.9


def calc_box_center_pos(box):
    return (box[0] + box[1]) / 2.0


class Track:
    class states(IntEnum):
        predicted = 0
        measured = 1
        validated = 2

    def __init__(
        self, id, pos, appearance, existance, stamp, detectionIdx, posBufSize, appearanceBufSize
    ):
        self.detectsPosBuffer = []
        self.appearanceBuffer = []
        self.id = id
        self.trackingCount = 0
        self.detectsPosBuffer.append(pos)
        self.appearanceBuffer.append(appearance)
        self.appearance = appearance
        self.existance = existance
        self.stamp = stamp
        boxCenter = calc_box_center_pos(pos)
        self.posGaussian = GaussianState([[boxCenter], [0]], np.diag([50, 5]), timestamp=stamp)
        self.state = self.states.measured
        self.posBufSize = posBufSize
        self.appearanceBufSize = appearanceBufSize
        self.assocDetIdx = detectionIdx

    def addNewDetectionPos(self, pos):
        self.detectsPosBuffer.append(pos)
        if len(self.detectsPosBuffer) > self.posBufSize:
            self.detectsPosBuffer.pop(0)  # remove oldest

    def addNewAppearance(self, appearance):
        self.appearanceBuffer.append(appearance)
        if len(self.appearanceBuffer) > self.appearanceBufSize:
            self.appearanceBuffer.pop(0)  # remove oldest

    def setAppearance(self, appearance):
        self.appearance = appearance

    def getAppearance(self):
        return np.mean(self.appearanceBuffer[:], axis=0)  # filter appearance over time

    def getDetectionBox(self):
        return self.detectsPosBuffer[-1]

    def getAveragePos(self):
        return np.mean(self.detectsPosBuffer, axis=0)

    def updateExistance(self, existDelta):
        self.existance = self.existance + existDelta
        self.existance = min(self.existance, 1.0)
        self.existance = max(self.existance, 0.0)

    def getStamp(self):
        return self.stamp

    def getTrackPos(self):
        return self.posGaussian

    def getTrackPosVar(self, useKalman):
        if useKalman:
            return self.posGaussian.covar[0][0]
        else:
            posMeans = np.mean(self.detectsPosBuffer, axis=1)
            var = np.var(posMeans)
            return var

    def setAssocDetIdx(self, detectionIdx):
        self.assocDetIdx = detectionIdx

    def getAssocDetIdx(self):
        return self.assocDetIdx

    def getId(self):
        return self.id

    def getState(self):
        return self.state


class ImageDetection:
    def __init__(self, box, azimuth, appearance, image, stamp):
        self.box = box
        self.azimuth = azimuth
        self.appearance = appearance
        self.stamp = stamp
        self.image = image

    def getAppearance(self):
        return self.appearance

    def getDetectionBox(self):
        return self.box

    def getStamp(self):
        return self.stamp

    def getAzimuth(self):
        return self.azimuth

    def getImage(self):
        return self.image


class KalmanTracker:
    def __init__(self, noiseCoeff, measPosVar):
        self.transition_model = ConstantVelocity(
            noiseCoeff
        )  # x, dx , NO y! => only track along x axis with position and speed
        self.predictor = KalmanPredictor(self.transition_model)
        self.measurement_model = LinearGaussian(
            ndim_state=2,  # Number of state dimensions (position and velocity in 1D)
            mapping=[0],  # Mapping measurement vector index to state index
            noise_covar=np.array(
                [[measPosVar]]
            ),  # Covariance matrix for Gaussian PDF of the measurement
        )
        self.updater = KalmanUpdater(self.measurement_model)

    def predict(self, gaussian, stamp):
        return self.predictor.predict(gaussian, timestamp=stamp)

    def update(self, gaussian, measurement):
        hypothesis = SingleHypothesis(gaussian, measurement)
        updatedGaussian = self.updater.update(hypothesis)
        return updatedGaussian


class BoatTracker:
    def __init__(self, params):
        self._params = params
        self._debug = self._params["debug"]
        self.tracks = []
        self.trackId = 0
        self.useKalman = self._params["tracking_kalman_use"]
        if self.useKalman:
            self.kalmanTracker = KalmanTracker(
                self._params["tracking_kalman_noise_coeff"],
                self._params["tracking_kalman_measurment_mdl_pos_var"],
            )

    def getNewTrackId(self):
        self.trackId = self.trackId + 1
        return self.trackId - 1

    def calc_gradient_img(self, img):
        ddepth = cv2.CV_16S
        kw = dict(
            ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT
        )  # BORDER_DEFAULT == BORDER_REFLECT_101 => replicate pixel outside image
        grad_x = cv2.Sobel(img, ddepth, 1, 0, **kw)
        grad_y = cv2.Sobel(img, ddepth, 0, 1, **kw)
        grad_x = np.abs(grad_x)
        grad_y = np.abs(grad_y)
        abs_grad_x = np.uint8(grad_x)
        abs_grad_y = np.uint8(grad_y)
        sobel = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
        # sobel_no_blend = cv2.add(abs_grad_x, abs_grad_y)
        # cv2.imshow('sobel', sobel)
        # cv2.waitKey(1)
        return sobel

    def calc_feature_vec(self, detection_img, detection_box):  # noqa: ARG002
        candidate_roi_img = detection_img  # roi[:, candidate_roi[0]: candidate_roi[1], :]
        chan_blue, chan_green, chan_red = cv2.split(candidate_roi_img)
        candidate_roi_gradients = self.calc_gradient_img(
            cv2.cvtColor(candidate_roi_img, cv2.COLOR_BGR2GRAY)
        )
        # TODO: Add features which only describing the segmented detection.
        #       Otherwise, lots of FP associations occur as the ROI mostly
        #       only contains water with horizon.
        # feat_boxSize_x = np.array(
        #    [np.arange(detection_box[0], detection_box[1])] * detection_img.shape[0]
        # ).flatten()
        feat_r = chan_red.flatten()
        feat_g = chan_green.flatten()
        feat_b = chan_blue.flatten()
        feat_gradients = candidate_roi_gradients.flatten()
        feat_vec = np.array(
            [
                # feat_boxSize_x,
                feat_r,
                feat_g,
                feat_b,
                feat_gradients,
            ]
        )
        return feat_vec

    def calc_covar(self, values):
        """
        TODO: Speedup via "it is possible to compute covariance matrix from featureimages
              in a very fast way using integral image represen-tation [11]. "
        """
        return np.cov(values)

    def calc_covar_distance(self, c1, c2):
        # distance / assoc appearance likelihood is calculated using approach from
        # "covariance Tracking using ModelUpdate Based on Means on Riemannian Manifolds" paper
        # its patented but we can use it for now
        lambda_ks = linalg.eig(a=c1, b=c2, left=False, right=False)  # lambda_k´s in the paper
        sum = 0
        for feat_idx, lambda_k in enumerate(lambda_ks):
            sum = sum + np.log(lambda_k.real) ** 2
        dist = np.sqrt(sum)
        return dist

    def associate(self, costs, associations, gateThreshold):
        # Calculate best fit based on costs (see below) by using the hungarian algorithm
        det_idx, track_idx = linear_sum_assignment(costs)  # using scipy
        # TODO calc using stonesoup (maybe slower than optimized scipy code?)

        for oneDet_idx, associatedTrack_idx in zip(det_idx, track_idx):
            # print(costs[oneDet_idx,associatedTrack_idx])
            if costs[oneDet_idx, associatedTrack_idx] < gateThreshold:
                associations[oneDet_idx] = associatedTrack_idx
        return associations

    def assoc_detection_2_tracks(self, detections, tracks):
        associations = np.array(np.ones(len(detections)) * NOT_ASSOC, int)
        gatePixelSize = self._params["tracking_assoc_gate_width"]
        gateThreshold = self._params["tracking_assoc_dist_threshold"]
        if len(tracks) > 0:
            costs = self.calc_assoc_costMatrix(gatePixelSize, tracks, detections)  #
            self.associate(costs, associations, gateThreshold)
        return associations

    def calc_assoc_costMatrix(self, gatePixelDist, tracks, detections):
        costs = np.ones(shape=[len(detections), len(tracks)]) * HUGE_COSTS
        for trackIdx, oneTrack in enumerate(self.tracks):
            if self.useKalman is False:
                trackBox = oneTrack.getDetectionBox()
                gateMin = trackBox[0] - gatePixelDist / 2.0
                gateMax = trackBox[1] + gatePixelDist / 2.0
            if self.useKalman is True:
                trackBox = oneTrack.getDetectionBox()
                boxWidth = trackBox[1] - trackBox[0]
                trackPos = oneTrack.posGaussian.mean[0][0]
                gateMin = trackPos - boxWidth / 2.0 - gatePixelDist / 2.0
                gateMax = trackPos + boxWidth / 2.0 + gatePixelDist / 2.0

            for detectionIdx, oneDetection in enumerate(detections):
                detectionBox = oneDetection.getDetectionBox()
                if detectionBox[0] > gateMin and detectionBox[1] < gateMax:
                    positionDist = abs(
                        calc_box_center_pos(oneTrack.getDetectionBox())
                        - calc_box_center_pos(oneDetection.getDetectionBox())
                    ) / (gatePixelDist / 2.0)
                    if positionDist > 0.0:
                        # Appearance similarity is not normalized -
                        # position similarity is normalized.
                        appearanceDist = self.calc_covar_distance(
                            oneTrack.getAppearance(), oneDetection.getAppearance()
                        )
                    else:
                        appearanceDist = 0
                    dist = appearanceDist * positionDist
                    costs[detectionIdx, trackIdx] = dist
        return costs

    def update_tracks(self, detections, tracks, predictedTracks, associatons):
        for detIdx, oneAssoc in enumerate(associatons):
            if oneAssoc != -1:
                detection = detections[detIdx]
                assocTrack = tracks[oneAssoc]
                assocTrack.state = Track.states.measured
                assocTrack.addNewDetectionPos(detection.getDetectionBox())
                assocTrack.addNewAppearance(detection.getAppearance())
                assocTrack.updateExistance(self._params["tracking_updater_valid_assoc_exist"])
                if self.useKalman is True:
                    measurement = TrackDetection(
                        np.array([[calc_box_center_pos(detection.getDetectionBox())]]),
                        timestamp=detection.getStamp(),
                    )
                    newGaussian = self.kalmanTracker.update(
                        predictedTracks[oneAssoc].posGaussian, measurement
                    )
                    assocTrack.posGaussian = newGaussian
                assocTrack.setAssocDetIdx(detIdx)

        for trackIdx, oneTrack in enumerate(tracks):
            if trackIdx not in associatons:
                oneTrack.updateExistance(self._params["tracking_updater_no_assoc_exist"])
                if self.useKalman is True:
                    oneTrack.posGaussian = predictedTracks[trackIdx].posGaussian
                oneTrack.setAssocDetIdx(-1)  # reset association idx

    def remove_double_tracks(self, tracks):
        doubles = []
        gatePixelSize = 100
        gateThreshold = 0.01
        if len(tracks) > 0:
            costs = self.calc_assoc_costMatrix(gatePixelSize, tracks, tracks)
            for i, _ in enumerate(tracks):
                for j, _ in enumerate(tracks):
                    if costs[i][j] < gateThreshold and i != j:
                        doubles.append((i, j))
        logger.info("doubles: %s", doubles)
        # actual remove of doubles to be implemented

    def propose_tracks(self, detections, tracks, associatons):
        for detIdx, oneAssoc in enumerate(associatons):
            if oneAssoc == -1:
                detection = detections[detIdx]
                proposedTrack = Track(
                    self.getNewTrackId(),
                    detection.getDetectionBox(),
                    detection.getAppearance(),
                    self._params["tracking_proposer_exist"],
                    detection.getStamp(),
                    detIdx,
                    self._params["tracking_track_pos_Buf_size"],
                    self._params["tracking_track_appearance_Buf_size"],
                )
                tracks.append(proposedTrack)

    def remove_tracks(self, tracks):
        filteredTracks = []
        for oneTrack in tracks:
            if (
                oneTrack.existance > self._params["tracking_remover_exist_thres"]
                and oneTrack.getTrackPosVar(self.useKalman)
                < self._params["tracking_remover_pos_var_thres"]
            ):
                filteredTracks.append(oneTrack)
        self.tracks = filteredTracks

    def predict_tracks(self, stamp):
        predictedTracks = []
        for oneTrack in self.tracks:
            oneTrack.state = Track.states.predicted
            trackGaussian = oneTrack.getTrackPos()
            predictedTrackGaussian = self.kalmanTracker.predict(trackGaussian, stamp=stamp)

            trackBoxSize = oneTrack.getDetectionBox()[1] - oneTrack.getDetectionBox()[0]
            predictedTrack = copy.copy(oneTrack)
            predictedTrack.addNewDetectionPos(
                (
                    int(predictedTrackGaussian.mean[0] - trackBoxSize / 2),
                    int(predictedTrackGaussian.mean[0] + trackBoxSize / 2),
                )
            )
            predictedTracks.append(predictedTrack)
            predictedTrack.posGaussian = predictedTrackGaussian

        return predictedTracks

    def validate_tracks(self):
        for oneTrack in self.tracks:
            trackPosVar = oneTrack.getTrackPosVar(self.useKalman)
            trackExistance = oneTrack.existance
            if oneTrack.state == Track.states.validated or oneTrack.state == Track.states.measured:
                if (
                    trackPosVar < self._params["tracking_validation_pos_var_tresh"]
                    and trackExistance > self._params["tracking_validation_exist_tresh"]
                ):
                    oneTrack.state = Track.states.validated
                else:
                    oneTrack.state = Track.states.measured
            # else if oneTrack.state == Track.states.predicted:
            #    oneTrack.state = Track.states.predicted

    def track_detections(self, detections, roi, stamp):
        stamp_datetime = datetime.fromtimestamp(stamp)  # datetime format needed by stonesoup

        # calc detection appearance/covar for tracking
        for detection in detections:
            detection_feat_vec = self.calc_feature_vec(
                detection.getImage(), detection.getDetectionBox()
            )  # self.calc_feature_vec(roi, detection)
            detection.appearance = self.calc_covar(detection_feat_vec)

        # assoc detections to tracks
        predictedTracks = None
        if self.useKalman is True:
            # predict new track pos using constant velocity model
            predictedTracks = self.predict_tracks(stamp_datetime)
            associatons = self.assoc_detection_2_tracks(detections, predictedTracks)
        if self.useKalman is False:
            # We assume the detections stay at some position over time in camera image.
            # TODO: Problem when moving camera?
            for oneTrack in self.tracks:
                oneTrack.state = Track.states.predicted
            associatons = self.assoc_detection_2_tracks(detections, self.tracks)

        # update tracks with associated detections
        self.update_tracks(detections, self.tracks, predictedTracks, associatons)

        # create new tracks for unassociated detections
        self.propose_tracks(detections, self.tracks, associatons)

        # remove tracks which dont fullfill specific tracking criteria
        self.remove_tracks(self.tracks)

        # remove double tracks
        # self.remove_double_tracks(self.tracks) # not needed for now

        # validate tracked objects by using track statistics
        self.validate_tracks()

        if self._debug:
            roi_view = cv2.resize(roi, (1200, 60))

            # Draw detections
            for index, detection in enumerate(detections):
                cv2.rectangle(
                    roi_view,
                    (int(detection[0][0]), int(0.2 * roi_view.shape[0])),
                    (int(detection[0][1]), int(0.8 * roi_view.shape[0])),
                    (0, 0, 255),
                    1,
                )

            for oneTrack in self.tracks:
                colorValid = (0, 255, 0)
                colorMeasured = (0, 255, 255)
                colorPredicted = (255, 0, 0)
                colors = [colorPredicted, colorMeasured, colorValid]
                color = colors[oneTrack.state]

                trackPosVar = int(oneTrack.getTrackPosVar(self.useKalman))
                trackSpeed = 0
                trackDetPos = oneTrack.getDetectionBox()
                if self.useKalman:
                    trackPos = int(oneTrack.posGaussian.mean[0][0])
                    trackSpeed = int(oneTrack.posGaussian.mean[1][0]) * 1
                else:
                    trackPos = int(calc_box_center_pos(trackDetPos))
                trackId = oneTrack.id

                trackExistance = round(oneTrack.existance, 2)

                cv2.putText(
                    roi_view,
                    str(trackId),
                    (trackDetPos[1] + 10, int(0.2 * roi_view.shape[0])),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.3,
                    color,
                    1,
                )
                cv2.putText(
                    roi_view,
                    str(round(trackPosVar, 2)),
                    (
                        trackDetPos[1] + 10,
                        int(0.6 * roi_view.shape[0]),
                    ),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.3,
                    color,
                    1,
                )
                cv2.putText(
                    roi_view,
                    str(trackExistance),
                    (
                        trackDetPos[1] + 10,
                        int(0.8 * roi_view.shape[0]),
                    ),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.3,
                    color,
                    1,
                )

                cv2.line(
                    roi_view,
                    (trackPos + trackPosVar, int(0.4 * roi_view.shape[0])),
                    (trackPos + trackPosVar, int(0.6 * roi_view.shape[0])),
                    (255, 255, 0),
                    1,
                )
                cv2.line(
                    roi_view,
                    (trackPos - trackPosVar, int(0.4 * roi_view.shape[0])),
                    (trackPos - trackPosVar, int(0.6 * roi_view.shape[0])),
                    (255, 255, 0),
                    1,
                )

                cv2.line(
                    roi_view,
                    (trackPos, int(0.5 * roi_view.shape[0])),
                    (trackPos + trackSpeed, int(0.5 * roi_view.shape[0])),
                    color,
                    1,
                )
                cv2.line(
                    roi_view,
                    (trackPos, int(0.4 * roi_view.shape[0])),
                    (trackPos, int(0.6 * roi_view.shape[0])),
                    color,
                    1,
                )

                cv2.rectangle(
                    roi_view,
                    (trackDetPos[0], int(0.3 * roi_view.shape[0])),
                    (trackDetPos[1], int(0.7 * roi_view.shape[0])),
                    color,
                    1,
                )

            cv2.imshow("Tracking", roi_view)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                pass

        return self.tracks
