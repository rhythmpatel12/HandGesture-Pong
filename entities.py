import pygame

class Paddle:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width, self.height = 10, 140
        self.color = (200, 200, 200)
        self.x = self.screen_width - 20  # Initialize the x position
        self.y = self.screen_height / 2 - self.height / 2  # Initialize the y position to start in the middle

    def draw(self, screen, y):
        self.y = y  # Update the y position each time the paddle is drawn
        self.position = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.position)

class Ball:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 15
        self.x = screen_width / 2 - self.radius
        self.y = screen_height / 2 - self.radius
        self.color = (255, 69, 0)
        self.speed_x = 7  # Speed of the ball in the x direction
        self.speed_y = 7  # Speed of the ball in the y direction

    def check_collision(self, paddle):
        # Reverse the vertical direction of the ball if it hits the top or bottom edge
        if self.y - self.radius <= 0 or self.y + self.radius >= 530:
            self.speed_y *= -1
            return 0

        # Ball collision with the left side
        if self.x - self.radius <= 0:
            self.speed_x *= -1  # Bounce off the left side
            return 0
        
        # Ball collision with the paddle on the right
        if self.x + 2*self.radius >= paddle.x and self.y - self.radius >= paddle.y and self.y + self.radius <= paddle.y + paddle.height:
            self.speed_x *= -1  # Reverse direction if it hits the paddle
            return 1
        
        #Ball collision with the right side (missed paddle)
        if self.x + 2* self.radius >= 1280:
            self.speed_x *= -1
            return -1

        return 0 #default

        
    def move(self, paddle):
        self.x += self.speed_x
        self.y += self.speed_y
        return self.check_collision(paddle)
        
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, 2*self.radius, 2*self.radius))


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
        else:
            pause_message = self.font.render(f"No hand detected. Game Paused.", True, (255, 255, 255))
            screen.blit(pause_message, (450, self.screen_height - self.hud_height + 40))
