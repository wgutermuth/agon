import pygame
import time
import sys
import random
from settings import *

clock = pygame.time.Clock()

print(f" the quit event is type {pygame.QUIT}")
pygame.init()

# Font Settings
game_font = pygame.font.Font("assets/fonts/hogfish.otf", 128)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")

background = screen.copy()
def draw_background():
    background.fill(WATER_COLOR)
    text = game_font.render("Agon!", True, (17, 3, 64))
    background.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
draw_background()

#pygame.draw.rect(screen, (0,255,0), (200,200, 50,50))
#pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Thanks for playing")
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.blit(background, (0, 0))
    # Update the display
    pygame.display.flip()
    clock.tick(60)
