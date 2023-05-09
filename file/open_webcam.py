import cv2
"""
# Requirements
python --version     
Python 3.9.13
pip install opencv-python

# Execution
python open_webcam.py
"""

def open_webcam():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Webcam', frame)

        # Press 'q' to close the webcam window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_webcam()
