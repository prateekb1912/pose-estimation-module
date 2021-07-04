import mediapipe as mp


class PoseEstimator():

    def __init__(self, mode=False, up_body=False, smooth=True, det_conf=0.5, track_conf=0.5):

        self.mode = mode
        self.up_body = up_body
        self.smooth = smooth
        self.min_detect_conf = det_conf
        self.min_track_conf = track_conf

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.up_body, self.smooth,
                                     self.min_detect_conf, self.min_track_conf)
        self.mpDraw = mp.solutions.drawing_utils

        
