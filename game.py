import pygame
import sys
import numpy as np
from entities import Ball, Paddle, HUD, FlashEffect
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
        self.hud = HUD(self.screen_width, self.screen_height)
        self.flash_effect = FlashEffect(self.screen_width, self.screen_height)

    def run(self):
        clock = pygame.time.Clock()
        score = 0
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
                paddle_y = np.clip(paddle_y, 5, 400)
                self.paddle.draw(self.screen, paddle_y)
                 # Update game entities...
                point = self.ball.move(self.paddle)  # Move the ball and check for collisions
                if point == -1: 
                    self.flash_effect.trigger()
                score += point

           

            hand_present = len(hands) > 0
            self.ball.draw(self.screen)
            self.hud.draw(self.screen, score=score, hand_present=hand_present)
            self.flash_effect.update_and_draw(self.screen)

            pygame.display.flip()
            clock.tick(60)  # FPS