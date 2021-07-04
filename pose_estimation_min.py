import cv2
import numpy as np
import mediapipe as mp
import time

# Create our pose estiamtion model object
mpPose = mp.solutions.pose
pose = mpPose.Pose()    # keep all default parameters
mpDraw = mp.solutions.drawing_utils

# Initialize video capture object
cap = cv2.VideoCapture('smith.mp4')

prev = 0
# Start reading from the video file
while cv2.waitKey(1)!= 27:
    succ, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Pass our video frames as images to the model object
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    # Calculating FPS
    curr = time.time()
    fps = 1/(curr-prev)
    prev = curr

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, (0, 255, 255),2)

    print(results.pose_landmarks)

    cv2.imshow("Video", img)