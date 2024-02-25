import pygame

class Paddle:
    def __init__(self, screen_width, screen_height):
        self.width, self.height = 10, 140
        self.position = pygame.Rect(screen_width - 20, screen_height / 2 - 70, self.width, self.height)
        self.color = (200, 200, 200)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.position)

class Ball:
    def __init__(self, screen_width, screen_height):
        self.radius = 15
        self.position = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, self.radius * 2, self.radius * 2)
        self.color = (255 , 69 , 0)

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.position)
