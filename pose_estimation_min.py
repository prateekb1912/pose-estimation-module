import cv2
import numpy as np
import mediapipe as mp
import time

# Initialize video capture object
cap = cv2.VideoCapture('Footwork.mp4')

prev = 0
# Start reading from the video file
while cv2.waitKey(24)!= 27:
    succ, img = cap.read()

    # Calculating FPS
    curr = time.time()
    fps = 1/(curr-prev)
    prev = curr

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, (0, 255, 255),2)

    cv2.imshow("Video", img)