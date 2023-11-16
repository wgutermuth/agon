import pygame
import sys
from player import Player
from settings import *
from background import Background

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Font Settings
game_font = pygame.font.Font("assets/fonts/hogfish.otf", 64)

pygame.display.set_caption("Shipwreck Showdown")

background = Background(map="1")

walls = pygame.sprite.Group()

player1 = Player()

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
    player1.update(walls)

    # draw the game screen
    background.draw(screen)
    walls.draw(screen)
    player1.draw(screen)

    pygame.display.flip()
    clock.tick(60)