import cv2

class CameraCapture:
    def __init__(self, src=0):
        self.cap = cv2.VideoCapture(src)
        self.cap.set(3, 1280) #Resolution Width
        self.cap.set(4, 720) #Resolution Height
        self.cap.set(cv2.CAP_PROP_FPS, 30)  # Set frame rate to 30 fps

    def read(self):
        _, frame = self.cap.read()
        return frame

    def release(self):
        self.cap.release()