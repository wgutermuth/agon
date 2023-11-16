import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.player_image = pygame.image.load("assets/images/Ships/black_ship.png").convert()
        self.right_image = pygame.transform.rotate(self.player_image, 90)
        self.right_image.set_colorkey((0, 0, 0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.image = self.right_image
        # creating a rectangle that defines where to paint my fish
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_left:
            self.rect.x -= 2
            self.image = self.left_image
        elif self.moving_right:
            self.rect.x += 2
            self.image = self.right_image
        if self.moving_up:
            self.rect.y -= 2
        elif self.moving_down:
            self.rect.y += 2
        # make sure this puts the fish in a valid position
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT - 2 * TILE_SIZE:  # account for sand
            self.rect.bottom = SCREEN_HEIGHT - 2 * TILE_SIZE

    def draw(self, screen):
        screen.blit(self.image, self.rect)

player = pygame.sprite.Group()