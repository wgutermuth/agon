import pygame
import sys
import subprocess
from pygame.locals import QUIT

# Initialize Pygame modules
pygame.init()

# Load settings
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_FONT

# Constants
PLAY_BUTTON_COLOR = (0,0,0, 128)
TEXT_COLOR = (255, 255, 255)
PLAY_BUTTON_HOVER_COLOR = (255, 0, 0, 128)
BUTTON_RADIUS = 10

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Title Screen")

# Load background image
background = pygame.image.load("assets/images/title_image.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create Play button
play_button_font = pygame.font.Font(GAME_FONT, 64)
play_button_text = play_button_font.render("Play", True, TEXT_COLOR)
play_button_rect = play_button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Quit button
quit_button_font = pygame.font.Font(GAME_FONT, 64)
quit_button_text = play_button_font.render("Quit", True, TEXT_COLOR)
quit_button_rect = play_button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2+94))

# Create Title text
title_font = pygame.font.Font(GAME_FONT, 72)
title_text = title_font.render("Shipwreck Showdown: Pirate's Plunder", True, TEXT_COLOR)
title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2-94))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the mouse click is on the Play button
            if play_button_rect.collidepoint(event.pos): # https://www.pygame.org/docs/ref/rect.html
                subprocess.run(["python", "game.py"]) # https://www.w3docs.com/snippets/python/how-can-i-make-one-python-file-run-another.html

                pygame.quit()
                sys.exit()

            if quit_button_rect.collidepoint(event.pos): # https://www.pygame.org/docs/ref/rect.html
                pygame.quit()
                sys.exit()

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the rounded and semi-transparent Play button
    pygame.draw.rect(screen, PLAY_BUTTON_COLOR, play_button_rect, border_radius=BUTTON_RADIUS)
    screen.blit(play_button_text, play_button_rect)
    pygame.draw.rect(screen, PLAY_BUTTON_COLOR, title_rect, border_radius=BUTTON_RADIUS)
    screen.blit(title_text, title_rect)
    pygame.draw.rect(screen, PLAY_BUTTON_COLOR, quit_button_rect, border_radius=BUTTON_RADIUS)
    screen.blit(quit_button_text, quit_button_rect)

    pygame.display.flip()