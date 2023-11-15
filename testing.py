import pygame
import sys
from settings import *

pygame.init()

# Font Settings
game_font = pygame.font.Font("assets/fonts/hogfish.otf", 64)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")

# Load your background image
original_background_image = pygame.image.load("assets/tiled/map1.png").convert()

# Resize the image to match the screen size
background_image = pygame.transform.scale(original_background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Thanks for playing")
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.blit(background_image, (0, 0))

    # Update the display
    pygame.display.flip()
