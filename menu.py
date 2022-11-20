# Main Menu Window

'''
Start-up file
Menu interface - has sound options + advance to chat session
'''

# ---------------------------------------------------------------------------------------------------------------------
# Imports

import os
import sys
import pygame

# ---------------------------------------------------------------------------------------------------------------------
# User Manual Function

def user_manual():
    pass

# ---------------------------------------------------------------------------------------------------------------------
# Main Function

def main():
    click = False
    while True:
        
        mx, my = pygame.mouse.get_pos() 
       
        # event loop
        click = False
        for event in pygame.event.get():    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        # window update
        pygame.display.flip()
        CLOCK.tick(60)
        SCREEN.blit(bg_image, (0,0))

# ---------------------------------------------------------------------------------------------------------------------
# Setup

pygame.init()
CLOCK = pygame.time.Clock()
SCREEN_WIDTH = 571
SCREEN_HEIGHT = 720 
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption('kAi')
current_dir = os.getcwd()
bg_image = pygame.image.load(f'{current_dir}/Images/main_menu.tif')
