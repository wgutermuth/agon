import pygame
from pygame.sprite import Sprite

class Obstacle(Sprite):
    def __init__(self, x, y, height, width):
        super().__init__()

        self.rect = pygame.rect.Rect(x,y,width,height)


    def draw(self, screen):
        pygame.draw.rect(screen,(255,255,255),self.rect)