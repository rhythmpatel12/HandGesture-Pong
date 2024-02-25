import pygame
import sys
import numpy as np
from entities import Ball, Paddle
from hand_detection import HandDetection

class Game:

    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 1280, 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Pong Game')
        self.bg_color = pygame.Color('grey12')
        self.paddle = Paddle(self.screen_width, self.screen_height)
        self.ball = Ball(self.screen_width, self.screen_height)
        self.hand_detector = HandDetection(detection_confidence=0.8, max_hands=1)


    def run(self):
        clock = pygame.time.Clock()
        while True:

            hands, _ = self.hand_detector.get_hands()

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Drawing
            self.screen.fill(self.bg_color)
            
            if hands:
                hand = hands[0]
                x, y, w, h = hand['bbox']
                paddle_y = y + h // 2 - self.paddle.height // 2
                paddle_y = np.clip(paddle_y, 20, 400)
                self.paddle.draw(self.screen, paddle_y)
            
            self.ball.draw(self.screen)

            pygame.display.flip()
            clock.tick(60)  # FPS