import pygame
from pygame.sprite import spritecollide
import sys
from player import Player
from settings import *
from background import Background
from cannon import CannonBall
from positions import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

cannon_balls = pygame.sprite.Group()

pygame.display.set_caption("Shipwreck Showdown")

background = Background(map="1")

# Define rectangle coordinates
start_point = (215, 0)
end_point = (772, 78)

# Create a sprite with a rectangle
rectangle_sprite = pygame.sprite.Sprite()
rectangle_sprite.image = pygame.Surface((end_point[0] - start_point[0], end_point[1] - start_point[1]))
rectangle_sprite.image.fill((255, 255, 255))  # Fill with white color
rectangle_sprite.rect = rectangle_sprite.image.get_rect(topleft=start_point)

player1 = Player()

cannonball_timer = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Thanks for playing")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.moving_left = True
            if event.key == pygame.K_RIGHT:
                player1.moving_right = True
            if event.key == pygame.K_UP:
                player1.moving_up = True
            if event.key == pygame.K_DOWN:
                player1.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player1.moving_left = False
            if event.key == pygame.K_RIGHT:
                player1.moving_right = False
            if event.key == pygame.K_UP:
                player1.moving_up = False
            if event.key == pygame.K_DOWN:
                player1.moving_down = False

    # Check if it's time to create a new cannonball
    current_time = pygame.time.get_ticks()
    if current_time - cannonball_timer >= CANNON_INTERVAL:
        new_cannon_ball = CannonBall(*LCANNON_MAP1_1, direction="left", speed=2)
        cannon_balls.add(new_cannon_ball)
        new_cannon_ball = CannonBall(*LCANNON_MAP1_2, direction="left", speed=2)
        cannon_balls.add(new_cannon_ball)
        new_cannon_ball = CannonBall(*LCANNON_MAP1_3, direction="left", speed=2)
        cannon_balls.add(new_cannon_ball)
        new_cannon_ball = CannonBall(*RCANNON_MAP1_1, direction="right", speed=2)
        cannon_balls.add(new_cannon_ball)
        new_cannon_ball = CannonBall(*DCANNON_MAP1_1, direction="down", speed=2)
        cannon_balls.add(new_cannon_ball)
        new_cannon_ball = CannonBall(*DCANNON_MAP1_2, direction="down", speed=2)
        cannon_balls.add(new_cannon_ball)
        new_cannon_ball = CannonBall(*UCANNON_MAP1_1, direction="up", speed=2)
        cannon_balls.add(new_cannon_ball)
        cannonball_timer = current_time  # Reset the timer
    # update game objects
    cannon_balls.update()
    player1.update()

    # draw the game screen
    background.draw(screen)
    player1.draw(screen)
    cannon_balls.draw(screen)

    player_hit_list = spritecollide(player1, cannon_balls, True)  # The third parameter (True) removes the cannonball on collision
    if player_hit_list:
        player1.die()

    pygame.display.flip()
    clock.tick(60)