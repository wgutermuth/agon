import pygame
import sys
import player
from settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Font Settings
game_font = pygame.font.Font("assets/fonts/hogfish.otf", 64)

pygame.display.set_caption("Shipwreck Showdown")

# Load background image
original_background_image = pygame.image.load("assets/tiled/map1.png").convert()
# Resize the image to match the screen size
background_image = pygame.transform.scale(original_background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

player1 = player.Player()

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

    # update game objects
    player1.update()

    # draw the game screen
    screen.blit(background_image, (0, 0))
    player1.draw(screen)

    pygame.display.flip()
    clock.tick(60)