import pygame
import random
from settings import *

class Collectible(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/images/Entities/crew (1).png").convert_alpha()
        self.scaled_image = pygame.transform.scale(self.image, ( int(self.image.get_width() * SHIP_SCALING_FACTOR),int(self.image.get_height() * SHIP_SCALING_FACTOR)))
        self.rect = pygame.rect.Rect(random.randint(0, SCREEN_WIDTH - self.scaled_image.get_width()), random.randint(0, SCREEN_HEIGHT - self.scaled_image.get_height()),self.scaled_image.get_width(), self.scaled_image.get_height())

    def draw(self, screen):
        screen.blit(self.scaled_image, self.rect)