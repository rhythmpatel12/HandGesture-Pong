import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

from camera_capture import CameraCapture
from image_processor import load_image, blend_images

# Importing all images
imgBg = load_image("resources/Background.png")
imgBall = load_image("resources/Ball.png", cv2.IMREAD_UNCHANGED)
imgPad1 = load_image("resources/paddle1.png", cv2.IMREAD_UNCHANGED)
imgPad2 = load_image("resources/paddle2.png", cv2.IMREAD_UNCHANGED)



camera = CameraCapture()
while True:
    frame = camera.read()
    if frame is not None:
        # Process frame
        frameBg = cv2.addWeighted(frame, 0.2, imgBg, 0.8, 0)


        cv2.imshow('Frame', frameBg)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()