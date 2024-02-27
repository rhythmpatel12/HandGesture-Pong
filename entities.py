import pygame
import math 

class SoundEffect:
    """
    Handles loading and playing of sound effects.
    """
    def __init__(self):
        pygame.mixer.init()

        # Dictionary mapping sound names to Sound objects.
        self.sounds = {
            'paddle_hit': pygame.mixer.Sound('resources/paddle_hit.wav'),
            'wall_hit': pygame.mixer.Sound('resources/wall_hit.wav'),
        }

    def play_sound(self, sound_name):
        """
        Plays the specified sound if it exists in the sounds dictionary.
        """
        if sound_name in self.sounds:
            self.sounds[sound_name].play()

class FlashEffect:
    """
    Manages a flash effect on the screen, used to indicate specific game events.
    """
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.active = False
        self.duration = 2  
        self.counter = 0
        self.color = (255, 0, 0, 32)

    def trigger(self):
        """
        Activates the flash effect.
        """
        self.active = True
        self.counter = self.duration

    def update_and_draw(self, screen):
        """
        Updates the effect's state and draws it on the screen if active.
        """
        if self.active:
            flash_surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
            flash_surface.fill(self.color)
            screen.blit(flash_surface, (0, 0))
            self.counter -= 1
            if self.counter <= 0:
                self.active = False


class Paddle:
    """
    Represents a paddle in the game, handling its drawing and position updates.
    """
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width, self.height = 10, 140
        self.color = (200, 200, 200)
        #Initialize the x and y position
        self.x = self.screen_width - 20 
        self.y = self.screen_height / 2 - self.height / 2
        #Attributes to track movement speed
        self.last_y = self.y
        self.movement_speed = 0  

    def update(self, y):
        """
        Updates the paddle's position and calculates its movement speed.
        """
        self.movement_speed = y - self.last_y
        self.last_y = y
        self.y = y

    def draw(self, screen, y):
        """
        Draws the paddle on the screen at its current position.
        """
        self.y = y
        self.position = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.position)

class Ball:
    """
    Represents the game ball, managing its movement, drawing, and collision detection.
    """
    def __init__(self, screen_width, screen_height, sound_effect=None):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 15
        self.x = screen_width / 2 - self.radius
        self.y = screen_height / 2 - self.radius
        self.color = (255, 69, 0)
        self.speed_x = 10  # Horizontal movement speed
        self.speed_y = 0  # Vertical movement speed
        self.sound_effect = sound_effect # SoundEffect instance for playing sounds.

    def check_collision(self, paddle):
        """
        Checks for and handles collisions with the paddle and screen edges, adjusting the ball's direction and speed, and returning a point value based on the collision outcome.
        """
        # Reverse the vertical direction of the ball if it hits the top or bottom edge (change direction)
        if self.y - self.radius <= 0 or self.y + self.radius >= 530:
            self.speed_y *= -1
            return 0

        # Ball collision with the left side (change direction, slight displacement)
        if self.x - self.radius <= 0:
            self.speed_x *= -1 
            self.x += 10  
            return 0
        
        # Ball collision with the paddle on the right (change direction, slight displacement, horizontal speedup, impart vertical momentum )
        if self.x + 2*self.radius >= paddle.x and self.y >= paddle.y and self.y + self.radius <= paddle.y + paddle.height:
            self.sound_effect.play_sound('paddle_hit')
            self.speed_x *= -1  
            self.x -= 20 
            self.speed_x -= 1

            # Modify the ball's vertical speed based on the paddle's movement speed
            self.speed_y += paddle.movement_speed * 0.2  # multiplier for gameplay balance
            return 1
        
        #Ball collision with the right side (missed paddle)
        if self.x + 2* self.radius >= 1270:
            self.sound_effect.play_sound('wall_hit')
            self.speed_x *= -1
            self.x -= 20 #displace ball 
            self.speed_x += 1 #decrease speed on collision
            return -1

        return 0 #default

        
    def move(self, paddle):
        """
        Updates the ball's position based on its speed and checks for collisions.
        """
        self.x += self.speed_x
        self.y += self.speed_y
        return self.check_collision(paddle)
        
    
    def draw(self, screen):
        """
        Draws the ball on the screen at its current position.
        """
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, 2*self.radius, 2*self.radius))


class HUD:
    """
    Represents the Heads-Up Display (HUD), showing game information such as score and hand detection status.
    """
    def __init__(self, screen_width, screen_height):
        self.font = pygame.font.Font(None, 36)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.hud_height = 200 
        self.hud_color = pygame.Color('black')
        # Color and size of camera indicator
        self.dot_color = pygame.Color('green')  
        self.dot_radius = 10  
        

    def draw(self, screen, score=0, hand_present=False): 
        """
        Draws the HUD on the screen which includes score and camera indication.
        """ 
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


class GravityWell:
    def __init__(self, x, y, strength, size=20, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.strength = strength
        self.size = size  # Size of the visual indicator
        self.color = color  # Color of the visual indicator

    def attract(self, obj):
        # Calculate the distance between the object and the gravity well
        distance_x = self.x - obj.x
        distance_y = self.y - obj.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        # Prevent the ball from getting "stuck" by setting a minimum effective distance
        min_distance = 100  # Adjust as needed for gameplay balance
        effective_distance = max(distance, min_distance)

        # Adjust the force to give an orbital effect rather than direct attraction
        # The force is calculated similarly but applied perpendicularly
        force = self.strength / (effective_distance**2 + 1)  # +1 to avoid division by zero

        # Calculate the direction of the force for a circular orbit
        # Swap and negate one coordinate to get a perpendicular direction
        force_x = force * distance_y / effective_distance
        force_y = force * distance_x / effective_distance

        # Apply the force to the object's velocity
        obj.speed_x += 0.5* force_x 
        obj.speed_y += 0.5* force_y 

    def draw(self, screen):
        # Draw the visual indicator as a circle
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

        # Optional: Draw a larger, semi-transparent circle to indicate the area of influence
        influence_radius = int(math.sqrt(self.strength))  # Example calculation
        surface = pygame.Surface((influence_radius*2, influence_radius*2), pygame.SRCALPHA)
        pygame.draw.circle(surface, self.color + (64,), (influence_radius, influence_radius), influence_radius)
        screen.blit(surface, (self.x - influence_radius, self.y - influence_radius))