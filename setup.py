import subprocess
import sys

def install_requirements():
    try:
        print("Installing requirements from requirements.txt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--quiet"])
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install requirements. Error: {e}")
        sys.exit(1)

install_requirements()

import cv2

def check_webcam():
    try:
        cap = cv2.VideoCapture(0) # 0 is usually the default webcam
        if cap is None or not cap.isOpened():
            print("No valid webcam found.")
            sys.exit(1)
        print("Webcam check passed.")
        cap.release()
    except Exception as e:
        print(f"Failed to access the webcam. Error: {e}")
        sys.exit(1)

    
check_webcam()
print("Setup completed successfully. You're all set to run the game!")