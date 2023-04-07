import cv2
import os
from datetime import datetime
"""
# Requirements
python --version     
Python 3.9.13
pip install opencv-python

# Execution
python take_webcam_picture.py
"""


def capture_picture(output_dir='/tmp/', filename=None):
    if not filename:
      # Set the default filename based on the current date and time
      filename = datetime.now().strftime('%Y%m%d-%H%M%S') + '.png'

    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        raise ValueError("Could not open webcam")

    # Read a frame from the webcam
    ret, frame = cap.read()
    output_file = os.path.join(output_dir, filename)

    # Save the captured frame to the output file
    cv2.imwrite(output_file, frame)

    # Release the webcam
    cap.release()

if __name__ == "__main__":
    # Capture a picture and save it to the default location
    capture_picture()
