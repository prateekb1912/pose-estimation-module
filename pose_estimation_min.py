import cv2
import numpy as np
import mediapipe as mp
import time

# Create our pose estiamtion model object
mpPose = mp.solutions.pose
pose = mpPose.Pose()    # keep all default parameters

# Initialize video capture object
cap = cv2.VideoCapture('Footwork.mp4')

prev = 0
# Start reading from the video file
while cv2.waitKey(1)!= 27:
    succ, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Pass our video frames as images to the model object
    results = pose.process(imgRGB)

    # Calculating FPS
    curr = time.time()
    fps = 1/(curr-prev)
    prev = curr

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, (0, 255, 255),2)

    cv2.imshow("Video", img)