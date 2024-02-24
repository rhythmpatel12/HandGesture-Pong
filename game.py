import cv2
import cvzone
from camera_capture import CameraCapture
from hand_detection import HandDetection
from image_processor import load_image
import numpy as np


class Game:
    def __init__(self):
        self.camera = CameraCapture()
        self.handDetection = HandDetection(detectionCon=0.8, maxHands=2)
        self.load_resources()

    def load_resources(self):
        self.imgBg = load_image("resources/Background.png")
        self.imgBall = load_image("resources/Ball.png", cv2.IMREAD_UNCHANGED)
        self.imgPad1 = load_image("resources/paddle1.png", cv2.IMREAD_UNCHANGED)
        self.imgPad2 = load_image("resources/paddle2.png", cv2.IMREAD_UNCHANGED)

    def run(self):
        
        
        

        while True:
            frame = self.camera.read()
            if frame is None:
                continue

            hands, processed_frame = self.handDetection.process_frame(frame)
            
            frameBg = cv2.addWeighted(processed_frame, 0.2, self.imgBg, 0.8, 0)
            
            #Game logic 

            #check for hands and add paddle
            if hands: 
                for hand in hands:

                    #align the position of the paddle with hand
                    x, y, w, h = hand['bbox']
                    h1, w1, _ = self.imgPad1.shape
                    y_hand = y - h1//2 
                    y_hand = np.clip (y1, 20, 415)


                    if hand['type'] == "Left":
                        frameBg = cvzone.overlayPNG(frameBg, self.imgPad1, (54,y_hand))

                    if hand['type'] == "Right":
                        frameBg = cvzone.overlayPNG(frameBg, self.imgPad2, (1190,y_hand))

            #add ball to frame 
            frameBg = cvzone.overlayPNG(frameBg, self.imgBall, (615,200))

            cv2.imshow('Game', frameBg)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.camera.release()
        cv2.destroyAllWindows()