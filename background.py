import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Background(pygame.sprite.Sprite):
    def __init__(self, map=1):
        super().__init__()
        self.map = map
        self.load_map_image()
        self.image = pygame.transform.scale(self.original_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()

    # My ambition was to have three maps, my patience was to have one map and many point categories.
    def load_map_image(self):
        if self.map == "1":
            self.original_image = pygame.image.load("assets/tiled/map1.png").convert()
        elif self.map == "2":
            self.original_image = pygame.image.load("assets/tiled/map2.png").convert()
        elif self.map == "3":
            self.original_image = pygame.image.load("assets/tiled/map3.png").convert()

    def draw(self, screen):
        screen.blit(self.image, self.rect)