# Main Menu Window

'''
Start-up file
Menu interface - has sound options, access to user_manual and advance to chat session
'''

# ---------------------------------------------------------------------------------------------------------------------
# Imports

import os
import sys
import pygame
import user_manual
import win32api
import win32con
import win32gui
import cwi

# ---------------------------------------------------------------------------------------------------------------------
# User Manual Function

def user_manual():
    um_images = [pic for pic in os.listdir(f'{current_dir}/images/user_manual_images/') if pic.endswith('.tif')]
    image_index = 0

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
bg_image = pygame.image.load(f'{current_dir}/images/main_menu.tif')

# ---------------------------------------------------------------------------------------------------------------------
# Runs Code

if __name__ == '__main__':
    main()
