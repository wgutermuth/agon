import pygame
from pygame.sprite import spritecollide
import sys
from player import Player
from settings import *
from background import Background
from cannon import CannonBall
from positions import *
from obstacle import Obstacle
from enemy import Enemy
import math

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

cannon_balls = pygame.sprite.Group()
player_cannon_balls = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
obstacles.add([Obstacle(220,0,80,540)])
obstacles.add([Obstacle(257,80,43,465)])
obstacles.add([Obstacle(300,123,45,425)])
obstacles.add([Obstacle(386,168,45,290)])
obstacles.add([Obstacle(386,213,40,210)])
obstacles.add([Obstacle(474,253,40,75)])
obstacles.add([Obstacle(732,517,400,460)])


pygame.display.set_caption("Shipwreck Showdown")

background = Background(map="1")

player1 = Player()

enemy_blue = Enemy("blue", 100, 200, "horizontal", [(10, 200), (380, 300)])
enemy_green = Enemy("green", 966, 270, "vertical", [(966, 6), (966, 503)])
enemy_red = Enemy("red", 1119, 400, "vertical", [(1119, 6), (1119, 503)])
enemy_yellow = Enemy("yellow", 492, 601, "horizontal", [(3, 601), (713, 601)])
enemies = pygame.sprite.Group([enemy_blue,enemy_green,enemy_red,enemy_yellow])

cannonball_timer = pygame.time.get_ticks()
enemy_cannonball_timer = pygame.time.get_ticks()

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
            if event.key == pygame.K_SPACE:
                player_fire_up = CannonBall(player1.rect.centerx, player1.rect.y - 10, direction="up", speed=2)
                player_cannon_balls.add(player_fire_up)

                player_fire_down = CannonBall(player1.rect.centerx, player1.rect.bottom, direction="down", speed=2)
                player_cannon_balls.add(player_fire_down)

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

    enemy_current_time = pygame.time.get_ticks()
    if enemy_current_time - enemy_cannonball_timer >= ENEMY_CANNON_INTERVAL:
        new_cannon_ball = CannonBall(enemy_blue.rect.centerx, enemy_blue.rect.bottom, direction="down", speed=2)
        cannon_balls.add(new_cannon_ball)
        new_cannon_ball = CannonBall(enemy_blue.rect.centerx, enemy_blue.rect.y - 10, direction="up", speed=2)
        cannon_balls.add(new_cannon_ball)
        # Vertical
        new_cannon_ball = CannonBall(enemy_red.rect.left, enemy_red.rect.centery, direction="left", speed=2)
        cannon_balls.add(new_cannon_ball)
        new_cannon_ball = CannonBall(enemy_red.rect.right, enemy_red.rect.centery, direction="right", speed=2)
        cannon_balls.add(new_cannon_ball)
        # Vertical
        new_cannon_ball = CannonBall(enemy_green.rect.left, enemy_green.rect.centery, direction="left", speed=2)
        cannon_balls.add(new_cannon_ball)
        new_cannon_ball = CannonBall(enemy_green.rect.right, enemy_green.rect.centery, direction="right", speed=2)
        cannon_balls.add(new_cannon_ball)
        new_cannon_ball = CannonBall(enemy_yellow.rect.centerx, enemy_yellow.rect.bottom, direction="down", speed=2)
        cannon_balls.add(new_cannon_ball)
        new_cannon_ball = CannonBall(enemy_yellow.rect.centerx, enemy_yellow.rect.y - 10, direction="up", speed=2)
        cannon_balls.add(new_cannon_ball)
        enemy_cannonball_timer = enemy_current_time

    # Update game objects
    cannon_balls.update()
    player_cannon_balls.update()
    player1.update()
    enemies.update()
    player_cannon_balls.update()

    # Draw the game screen
    background.draw(screen)
    player1.draw(screen)
    cannon_balls.draw(screen)
    enemies.draw(screen)

    player_hit_list = spritecollide(player1, cannon_balls, True)
    if player_hit_list:
        player1.die()

    enemy_red_hit_list = pygame.sprite.groupcollide(enemies, player_cannon_balls, True,True)
    if enemy_red_hit_list:
        enemies.die()

    player_hit_list = spritecollide(player1, obstacles, False)
    if player_hit_list:
        player1.die()

    pygame.display.flip()
    clock.tick(60)