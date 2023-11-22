import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.sprite import Sprite
from pygame.locals import Rect

class CannonBall(Sprite):
    def __init__(self, x, y, direction, speed):
        super().__init__()

        # Load cannonball image and scale it
        self.image = pygame.image.load("assets/images/Entities/cannonBall.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect(center=(x, y))

        # Set initial position and movement parameters
        self.rect.x = x
        self.rect.y = y
        self.direction = direction  # Specify the direction of movement (e.g., "left", "right", "up", "down")
        self.speed = speed  # Specify the speed of the cannonball

    def update(self):
        # Update the cannonball's position based on its direction and speed
        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed

        # Check if the cannonball is out of the screen
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:
            self.kill()  # Remove the cannonball sprite if it's out of the screen

    def draw(self, screen):
        screen.blit(self.image, self.rect)