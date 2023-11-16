import pygame
from settings import TILE_SIZE, SAND_BORDER_COLOR

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(SAND_BORDER_COLOR)
        self.rect = self.image.get_rect(topleft=(x, y))