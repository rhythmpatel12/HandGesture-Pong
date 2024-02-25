import pygame
import sys
from entities import Ball, Paddle

class Game:

    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 1280, 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Pong Game')
        self.bg_color = pygame.Color('grey12')
        self.paddle = Paddle(self.screen_width, self.screen_height)
        self.ball = Ball(self.screen_width, self.screen_height)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Drawing
            self.screen.fill(self.bg_color)
            
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)

            pygame.display.flip()
            clock.tick(60)  # FPS

if __name__ == "__main__":
    game = Game()
    game.run()