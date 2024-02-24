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
        self.ball_position = [615, 200]
        self.speedX = 10
        self.speedY = 10

    def load_resources(self):
        self.imgBg = load_image("resources/Background.png")
        self.imgBall = load_image("resources/Ball.png", cv2.IMREAD_UNCHANGED)
        self.imgPad1 = load_image("resources/paddle1.png", cv2.IMREAD_UNCHANGED)
        self.imgPad2 = load_image("resources/paddle2.png", cv2.IMREAD_UNCHANGED)

    def handle_paddle_movement(self, hands, frameBg):
        for hand in hands:
            x, y, w, h = hand['bbox']
            h1, w1, _ = self.imgPad1.shape
            y_hand = np.clip(y - h1 // 2, 20, 415)

            if hand['type'] == "Left":
                frameBg = cvzone.overlayPNG(frameBg, self.imgPad1, (54, y_hand))
                self.check_ball_collision(54, y_hand, w1, h1, "Left")

            elif hand['type'] == "Right":
                frameBg = cvzone.overlayPNG(frameBg, self.imgPad2, (1190, y_hand))
                self.check_ball_collision(1190 - 50, y_hand, w1, h1, "Right")
        return frameBg

    def check_ball_collision(self, paddle_x, paddle_y, paddle_w, paddle_h, paddle_side):
        if paddle_x < self.ball_position[0] < paddle_x + paddle_w and paddle_y < self.ball_position[1] < paddle_y + paddle_h:
            self.speedX *= -1
            if paddle_side == "Left":
                self.ball_position[0] += 15
            else:
                self.ball_position[0] -= 15

    def update_ball_position(self):
        if self.ball_position[1] >= 500 or self.ball_position[1] <= 15:
            self.speedY *= -1
        self.ball_position[0] += self.speedX
        self.ball_position[1] += self.speedY

    def run(self):
        while True:
            frame = self.camera.read()
            if frame is None:
                continue

            hands, processed_frame = self.handDetection.process_frame(frame)
            frameBg = cv2.addWeighted(processed_frame, 0.2, self.imgBg, 0.8, 0)

            if hands:
                frameBg = self.handle_paddle_movement(hands, frameBg)

            self.update_ball_position()
            frameBg = cvzone.overlayPNG(frameBg, self.imgBall, self.ball_position)

            cv2.imshow('Game', frameBg)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.camera.release()
        cv2.destroyAllWindows()

