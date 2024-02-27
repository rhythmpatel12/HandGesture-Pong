import pygame
import sys
import random
import numpy as np
from entities import Ball, Paddle, HUD, FlashEffect, SoundEffect, GravityWell
from hand_detection import HandDetection
from game_state import GameState

class Game:

    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 1280, 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Pong Game')
        self.bg_color = pygame.Color('grey12')

        self.flash_effect = FlashEffect(self.screen_width, self.screen_height)
        self.sound_effect = SoundEffect()

        self.paddle = Paddle(self.screen_width, self.screen_height)
        self.ball = Ball(self.screen_width, self.screen_height, sound_effect=self.sound_effect)
        self.hand_detector = HandDetection(detection_confidence=0.8, max_hands=1)
        self.hud = HUD(self.screen_width, self.screen_height)

        self.gravity_wells = [
            GravityWell(random.randint(50, 300), random.randint(50, 500), random.randint(4000,6000), size=random.randint(10, 20)),
            GravityWell(random.randint(300, 700), random.randint(50, 500), random.randint(4000,6000), size=random.randint(10, 20)),
            GravityWell(random.randint(700, 1000), random.randint(50, 500), random.randint(4000,6000), size=random.randint(10, 20))]
        
        self.state = GameState.START_SCREEN  # Initial state
        self.score = 0


    def run(self):
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            # Event handling
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Drawing
            self.screen.fill((0, 0, 0))  # Clear the screen

            if self.state == GameState.START_SCREEN:
                self.handle_start_screen(events)
            elif self.state == GameState.PLAYING_GAME:
                self.handle_playing_game(events)
            elif self.state == GameState.END_SCREEN:
                self.handle_end_screen(events)

            pygame.display.flip()
            clock.tick(60)  # FPS

    def handle_start_screen(self, events):
        # Implement start screen logic and rendering here
        start_text = pygame.font.Font(None, 36).render(f"Press SPACE to begin game", True, (255, 255, 255))

        self.screen.blit(start_text, (475, 350))  # Adjust positioning as needed
        # press Space to start the game
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = GameState.PLAYING_GAME

    def handle_playing_game(self, events):
        #game logic
        self.screen.fill(self.bg_color)

        hands, _ = self.hand_detector.get_hands()
        
        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            paddle_y = y + h // 2 - self.paddle.height // 2
            paddle_y = np.clip(paddle_y, 5, 400)
            self.paddle.draw(self.screen, paddle_y)

            # Determine the paddle's new Y position based on input or hand detection
            self.paddle.update(paddle_y)

            # Update game entities...
            point = self.ball.move(self.paddle)  # Move the ball and check for collisions
            if point == -1: 
                self.flash_effect.trigger()
            self.score += point

    

        hand_present = len(hands) > 0
        self.ball.draw(self.screen)
        self.hud.draw(self.screen, score=self.score, hand_present=hand_present)
        
        for well in self.gravity_wells:
            well.attract(self.ball)
            well.draw(self.screen)

        self.flash_effect.update_and_draw(self.screen)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = GameState.END_SCREEN

    def handle_end_screen(self, events):
        # Implement start screen logic and rendering here
        end_text = pygame.font.Font(None, 36).render(f"Press R to restart or Q to quit.", True, (255, 255, 255))

        self.screen.blit(end_text, (475, 400))  # Adjust positioning as needed

        score_text = pygame.font.Font(None, 46).render(f"Score: {self.score}", True, (255, 255, 255))

        self.screen.blit(score_text, (575, 350))  # Adjust positioning as needed

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.score = 0
                    self.state = GameState.PLAYING_GAME
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()