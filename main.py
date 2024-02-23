import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

from camera_capture import CameraCapture


# Usage
camera = CameraCapture()
while True:
    frame = camera.read()
    if frame is not None:
        # Process frame
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()