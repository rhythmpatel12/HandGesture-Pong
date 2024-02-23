import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True: 
    _, img = cap.read()
    cv2.imshow("Image", img)

    cv2.waitKey(1)