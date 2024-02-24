import cv2
from camera_capture import CameraCapture
from hand_detection import HandDetection
from image_processor import load_image


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
            # Game logic here, e.g., updating positions based on hand detection

            frameBg = cv2.addWeighted(processed_frame, 0.2, self.imgBg, 0.8, 0)
            cv2.imshow('Game', frameBg)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.camera.release()
        cv2.destroyAllWindows()