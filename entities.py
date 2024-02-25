import pygame

class Paddle:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width, self.height = 10, 140
        self.color = (200, 200, 200)

    def draw(self, screen, y):
        self.position = pygame.Rect(self.screen_width - 20, y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.position)

class Ball:
    def __init__(self, screen_width, screen_height):
        self.radius = 15
        self.position = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, self.radius * 2, self.radius * 2)
        self.color = (255 , 69 , 0)

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.position)

class HUD:
    def __init__(self, screen_width, screen_height):
        self.font = pygame.font.Font(None, 36)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.hud_height = 200 
        self.hud_color = pygame.Color('black')

        self.dot_color = pygame.Color('green')  # Color for the hand presence dot
        self.dot_radius = 10  # Size of the dot
        

    def draw(self, screen, score=0, hand_present=False):  
        pygame.draw.rect(screen, self.hud_color, (0, 550, self.screen_width, self.hud_height))
        
        # Display score or other information
        text_surface = self.font.render(f"Score: {score}", True, (255, 255, 255))

        screen.blit(text_surface, (10, self.screen_height - self.hud_height + 40))  # Adjust positioning as needed

        # Draw a green dot if a hand is present
        if hand_present:
            pygame.draw.circle(screen, self.dot_color, (self.screen_width - 30, self.screen_height - self.hud_height // 2), self.dot_radius)
