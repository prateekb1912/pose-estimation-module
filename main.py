import cv2
import argparse
from PoseModule import PoseEstimator

# Add command-line arguments parser
parser = argparse.ArgumentParser(description="Use the pose estimator module to use in your projects")
parser.add_argument('--video', '-V', type=str, nargs=1, help="Input video to draw estimated poses on")

args = parser.parse_args()

def main():
    # Initialize video capture object
    cap = cv2.VideoCapture(args['video'])

    detector = PoseEstimator()
    i = 0 
    
    # Start reading from the video file
    while cv2.waitKey(1) != 27:
        succ, img = cap.read()
        img = detector.findPose(img)
        
        cv2.imshow("Video", img)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()