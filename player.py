import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.player_image = pygame.image.load("assets/images/Ships/black_ship.png").convert()
        self.scaled_image = pygame.transform.scale(self.player_image, (int(self.player_image.get_width() * SHIP_SCALING_FACTOR), int(self.player_image.get_height() * SHIP_SCALING_FACTOR)))
        self.right_image = pygame.transform.rotate(self.scaled_image, 90)
        self.right_image.set_colorkey((0, 0, 0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.image = self.right_image
        # creating a rectangle that defines where to paint my fish
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.hit_counter = 0
        self.disable_input = False
        self.disable_input_timer = 0

    def update(self):
        if self.hit_counter < 3 and not self.disable_input:
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
            if self.rect.bottom > SCREEN_HEIGHT:  # account for sand
                self.rect.bottom = SCREEN_HEIGHT
            else:
                self.speed_x = 0
                self.speed_y = 0

                # Check if input needs to be disabled
                if self.disable_input_timer > 0:
                    self.disable_input_timer -= 1
                else:
                    self.disable_input = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def die(self):
        self.hit_counter += 1

        if self.hit_counter == 1:
            self.player_image = pygame.image.load("assets/images/Ships/black_ship_damaged.png").convert_alpha()
            self.scaled_image = pygame.transform.scale(self.player_image, (int(self.player_image.get_width() * SHIP_SCALING_FACTOR), int(self.player_image.get_height() * SHIP_SCALING_FACTOR)))
            self.right_image = pygame.transform.rotate(self.scaled_image, 90)
            self.left_image = pygame.transform.flip(self.right_image, True, False)
            if self.image == self.right_image:
                self.image = self.right_image
            else:
                self.image = self.left_image
        elif self.hit_counter == 2:
            self.player_image = pygame.image.load("assets/images/Ships/black_ship_damaged2.png").convert_alpha()
            self.scaled_image = pygame.transform.scale(self.player_image, (
            int(self.player_image.get_width() * SHIP_SCALING_FACTOR),
            int(self.player_image.get_height() * SHIP_SCALING_FACTOR)))
            self.right_image = pygame.transform.rotate(self.scaled_image, 90)
            self.left_image = pygame.transform.flip(self.right_image, True, False)
            if self.image == self.right_image:
                self.image = self.right_image
            else:
                self.image = self.left_image
        elif self.hit_counter == 3:
            self.player_image = pygame.image.load("assets/images/Ships/black_ship_destroyed.png").convert_alpha()
            self.scaled_image = pygame.transform.scale(self.player_image, (
            int(self.player_image.get_width() * SHIP_SCALING_FACTOR),
            int(self.player_image.get_height() * SHIP_SCALING_FACTOR)))
            self.right_image = pygame.transform.rotate(self.scaled_image, 90)
            self.left_image = pygame.transform.flip(self.right_image, True, False)
            if self.image == self.right_image:
                self.image = self.right_image
            else:
                self.image = self.left_image

    def bounce(self, enemy_rect):
        # Calculate the direction vector from player to enemy
        direction_vector = pygame.Vector2(enemy_rect.center) - pygame.Vector2(self.rect.center)
        direction_vector.normalize()

        # Bounce off by moving in the opposite direction
        self.speed_x = -direction_vector.x * BOUNCE_SPEED
        self.speed_y = -direction_vector.y * BOUNCE_SPEED

        self.disable_input_timer = 60

player = pygame.sprite.Group()