import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, x, y, direction, bounds, speed_x=2, speed_y=2):
        super().__init__()

        self.ship_image = pygame.image.load(f"assets/images/Ships/{color}_ship.png").convert_alpha()
        self.scaled_image = pygame.transform.scale(self.ship_image, (
            int(self.ship_image.get_width() * SHIP_SCALING_FACTOR),
            int(self.ship_image.get_height() * SHIP_SCALING_FACTOR)
        ))
        self.right_image = pygame.transform.rotate(self.scaled_image, 90)
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.image = self.right_image if direction == "horizontal" else self.scaled_image
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

        self.direction = direction
        self.bounds = bounds
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.hit_counter = 0
        self.color = color

    def update(self):
        if self.hit_counter <= 2:
            if self.direction == "horizontal":
                self.rect.x += self.speed_x
                if self.rect.left < self.bounds[0][0] or self.rect.right > self.bounds[1][0]:
                    self.speed_x = -self.speed_x
                    self.image = self.left_image if self.image == self.right_image else self.right_image
            elif self.direction == "vertical":
                self.rect.y += self.speed_y
                if self.rect.top < self.bounds[0][1] or self.rect.bottom > self.bounds[1][1]:
                    self.speed_y = -self.speed_y
                    self.image = pygame.transform.flip(self.image, False, True)

        # If hit counter is greater than 2, stop moving
        if self.hit_counter > 2:
            self.speed_x = 0
            self.speed_y = 0
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def die(self):
        self.hit_counter += 1

        if self.hit_counter <= 2:
            damage_levels = ["damaged2", "destroyed"]
            image_path = f"assets/images/Ships/{self.color}_ship_{damage_levels[self.hit_counter - 1]}.png"

            self.player_image = pygame.image.load(image_path).convert_alpha()
            self.scaled_image = pygame.transform.scale(self.player_image, (
                int(self.player_image.get_width() * SHIP_SCALING_FACTOR),
                int(self.player_image.get_height() * SHIP_SCALING_FACTOR)
            ))

            self.right_image = pygame.transform.rotate(self.scaled_image, 90)
            self.left_image = pygame.transform.flip(self.right_image, True, False)

            if self.direction == "horizontal":
                self.image = self.right_image if self.image == self.right_image else self.left_image
            elif self.direction == "vertical":
                # Check if the enemy is moving up or down before flipping the image
                if self.speed_y > 0:  # Moving down
                    self.image = self.scaled_image
                elif self.speed_y < 0:  # Moving up
                    self.image = pygame.transform.flip(self.scaled_image, False, True)

    def kill(self):
        self.die()
