import pygame
from settings import *

def draw_background(background_path):
    # Load background image
    original_background_image = pygame.image.load(background_path).convert()
    # Resize the image to match the screen size
    background_image = pygame.transform.scale(original_background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    #  Load title
    text = game_font.render("Chomp!", True, (255, 69, 0))

    background.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))