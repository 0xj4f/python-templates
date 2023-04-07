from PIL import ImageGrab
import os
from datetime import datetime

"""
# Requirements
python --version     
Python 3.9.13
pip install Pillow

# Execution
python capture_screenshot.py
"""


def capture_screenshot(output_dir='/tmp', filename=None):
    if not filename:
        # Set the default filename based on the current date and time
        filename = datetime.now().strftime('%Y%m%d-%H%M%S') + '.png'

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Combine output directory and filename
    output_file = os.path.join(output_dir, filename)

    # Capture the screenshot
    screenshot = ImageGrab.grab()

    # Save the screenshot to the output file
    screenshot.save(output_file)
    return output_file

if __name__ == "__main__":
    # Capture a screenshot and save it to the default location and filename
    print(capture_screenshot())

"""
Notes:
Execution must have the right permission
"""