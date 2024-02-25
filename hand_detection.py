import cv2
from cvzone.HandTrackingModule import HandDetector

class HandDetection:
    def __init__(self, detection_confidence=0.8, max_hands=1):
        self.cap = cv2.VideoCapture(0)
        self.detector = HandDetector(detectionCon=detection_confidence, maxHands=max_hands)

    def get_hands(self):
        success, img = self.cap.read()
        if not success:
            return [], img  # Return empty list and None if frame read was not successful
        img = cv2.flip(img, 1)  # Mirror the image
        hands, img = self.detector.findHands(img, flipType=False, draw=False)
        return hands, img
    
    def release(self):
        self.cap.release()

