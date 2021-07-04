import mediapipe as mp
import cv2 

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

    def findPose(self, img):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgRGB)

        if results.pose_landmarks:
            self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        
        return img

    