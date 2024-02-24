import cv2
from cvzone.HandTrackingModule import HandDetector

class HandDetection:
    def __init__(self, detectionCon=0.8, maxHands=2):
        self.detector = HandDetector(detectionCon=detectionCon, maxHands=maxHands)

    def process_frame(self, frame):
        frame = cv2.flip(frame, 1)
        hands, frame = self.detector.findHands(frame, flipType=False)  # with draw
        return hands, frame
