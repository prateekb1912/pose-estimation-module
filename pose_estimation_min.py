import cv2
import numpy as np
import mediapipe as mp

# Initialize video capture object
cap = cv2.VideoCapture('Footwork.mp4')

# Start reading from the video file
while True:
    succ, img = cap.read()
    cv2.imshow("Video", img)
    cv2.waitKey(1)