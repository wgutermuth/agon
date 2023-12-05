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
from collectible import Collectible
import math
import time

pygame.init()
pygame.mixer.init()
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
collectibles = pygame.sprite.Group([Collectible() for i in range(2)])


pygame.display.set_caption("Shipwreck Showdown")

background = Background(map="1")
pygame.mixer.music.load('assets/audio/pirate_music.mp3')
pygame.mixer.music.play(-1)
cannon_sound = pygame.mixer.Sound('assets/audio/multi_cannon.mp3')
cannon_sound.set_volume(0.5)

player1 = Player()
points = 0

enemy_blue = Enemy("blue", 100, 200, "horizontal", [(10, 200), (380, 300)])
enemy_green = Enemy("green", 966, 270, "vertical", [(966, 6), (966, 503)])
enemy_red = Enemy("red", 1119, 400, "vertical", [(1119, 6), (1119, 503)])
enemy_yellow = Enemy("yellow", 492, 601, "horizontal", [(3, 601), (713, 601)])
enemies = pygame.sprite.Group([enemy_blue,enemy_green,enemy_red,enemy_yellow])

cannonball_timer = pygame.time.get_ticks()
enemy_cannonball_timer = pygame.time.get_ticks()
spacebar_cooldown = pygame.time.get_ticks()
mouse_click_cooldown = pygame.time.get_ticks()

while True:
    current_time = pygame.time.get_ticks()
#    broadside_cooldown = BROADSIDE_COOLDOWN
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Thanks for playing")
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1.moving_left = True
            if event.key == pygame.K_d:
                player1.moving_right = True
            if event.key == pygame.K_w:
                player1.moving_up = True
            if event.key == pygame.K_s:
                player1.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player1.moving_left = False
            if event.key == pygame.K_d:
                player1.moving_right = False
            if event.key == pygame.K_w:
                player1.moving_up = False
            if event.key == pygame.K_s:
                player1.moving_down = False
            if event.key == pygame.K_SPACE:
                if current_time - spacebar_cooldown >= 1000:  # Spacebar cooldown is 1 second
                    player_fire_up = CannonBall(player1.rect.centerx, player1.rect.y - 10, direction="up", speed=2)
                    player_cannon_balls.add(player_fire_up)

                    player_fire_down = CannonBall(player1.rect.centerx, player1.rect.bottom, direction="down", speed=2)
                    player_cannon_balls.add(player_fire_down)

                    spacebar_cooldown = current_time  # Reset the cooldown timer
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if current_time - mouse_click_cooldown >= 2000:  # Mouse click cooldown is 2 seconds
                    # Calculate angle between player and mouse click
                    mouse_x, mouse_y = event.pos
                    player_x, player_y = player1.rect.center
                    angle = math.atan2(mouse_y - player_y, mouse_x - player_x)

                    # Launch cannonball in the direction of the mouse click
                    player_fire = CannonBall(player_x, player_y, direction=angle, speed=1)
                    player_cannon_balls.add(player_fire)
                    cannon_sound.play()
                    mouse_click_cooldown = current_time

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
        cannon_sound.play()
        cannonball_timer = current_time  # Reset the timer

    enemy_current_time = pygame.time.get_ticks()
    if enemy_current_time - enemy_cannonball_timer >= ENEMY_CANNON_INTERVAL:
        if enemy_blue.hit_counter < 2:
            new_cannon_ball = CannonBall(enemy_blue.rect.centerx, enemy_blue.rect.bottom, direction="down", speed=2)
            cannon_balls.add(new_cannon_ball)
            new_cannon_ball = CannonBall(enemy_blue.rect.centerx, enemy_blue.rect.y - 10, direction="up", speed=2)
            cannon_balls.add(new_cannon_ball)
        # Vertical
        if enemy_red.hit_counter < 2:
            new_cannon_ball = CannonBall(enemy_red.rect.left, enemy_red.rect.centery, direction="left", speed=2)
            cannon_balls.add(new_cannon_ball)
            new_cannon_ball = CannonBall(enemy_red.rect.right, enemy_red.rect.centery, direction="right", speed=2)
            cannon_balls.add(new_cannon_ball)
        # Vertical
        if enemy_green.hit_counter < 2:
            new_cannon_ball = CannonBall(enemy_green.rect.left, enemy_green.rect.centery, direction="left", speed=2)
            cannon_balls.add(new_cannon_ball)
            new_cannon_ball = CannonBall(enemy_green.rect.right, enemy_green.rect.centery, direction="right", speed=2)
            cannon_balls.add(new_cannon_ball)
        if enemy_yellow.hit_counter < 2:
            new_cannon_ball = CannonBall(enemy_yellow.rect.centerx, enemy_yellow.rect.bottom, direction="down", speed=2)
            cannon_balls.add(new_cannon_ball)
            new_cannon_ball = CannonBall(enemy_yellow.rect.centerx, enemy_yellow.rect.y - 10, direction="up", speed=2)
            cannon_balls.add(new_cannon_ball)
        cannon_sound.play()
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
    player_cannon_balls.draw(screen)
    enemies.draw(screen)

    # Display the point counter at the top right of the screen
    font = pygame.font.Font(GAME_FONT, 64)
    point_text = font.render(f"Points: {points}", True, (255, 255, 255))
    point_rect = point_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
    screen.blit(point_text, point_rect)

    player_hit_list = spritecollide(player1, cannon_balls, True)
    if player_hit_list:
        player1.die()

    enemy_hit_list = pygame.sprite.groupcollide(enemies, player_cannon_balls, False,True)
    for enemy in enemy_hit_list:
        enemy.die()
        if enemy.hit_counter == 2:  # Each enemy has 2 hit points.
            points += 1

    player1.collect(collectibles)
    collectibles.draw(screen)

    player_hit_list = spritecollide(player1, obstacles, False)
    if player_hit_list:
        player1.die()

    if points >= 4:
        win_font = pygame.font.Font(GAME_FONT, 100)
        win_text = win_font.render("YOU WIN!", True, (255, 255, 255))
        win_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(win_text, win_rect)

        # Display for 3 seconds before quitting the game
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    if player1.hit_counter >= 3:
        game_over_font = pygame.font.Font(GAME_FONT, 128)
        game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, game_over_rect)

        # Display for 3 seconds before quitting the game
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(60)