# User Manual

'''
Provides a slideshow display of how to use the application
Can be access from the main menu, and the chat window
'''

# ---------------------------------------------------------------------------------------------------------------------
# Imports

import os
import sys
import pygame
import menu
from menu import SCREEN
from menu import CLOCK

# ---------------------------------------------------------------------------------------------------------------------
# Utility Functions

def draw_rect_transparent(surface, colour, rect):
    '''
    Draws transparent rectangles on given surface
    '''

    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA) # makes a surface from rectangles of given rectangles, with alpha property
    pygame.draw.rect(shape_surf, colour, shape_surf.get_rect()) # draws rectangle using surface
    surface.blit(shape_surf, rect)

# ---------------------------------------------------------------------------------------------------------------------
# User Manual Function

def um_main():
    '''
    Runs the user manual, displays a slideshow of images that loops
    Has special case buttons that work on a specific slide (slide 0)
    Can be exited to return to main menu at any point by pressing the ESC key
    '''

    # setup
    current_dir = os.getcwd()
    um_images = [pic for pic in os.listdir(f'{current_dir}/images/user_manual_images/') if pic.endswith('.tif')]
    click = False
    image_index = 0
    
    # click boxes
    home_icon = pygame.Rect(10, 7, 27, 24)
    quit_icon = pygame.Rect(1249, 7, 23, 23)

    running = True
    while running:
        mx, my = pygame.mouse.get_pos()

        # drawing click boxes
        draw_rect_transparent(SCREEN, (0, 0, 0, 0), home_icon)
        draw_rect_transparent(SCREEN, (0, 0, 0, 0), quit_icon)

        # ---------------------------------------------------------------------------------------------------------------------
        # Events

        click = False
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # special case on slide 0, home icon and quit icon 
        if image_index == 0:
            if home_icon.collidepoint(mx, my):
                if click:
                    menu.main()
            if quit_icon.collidepoint(mx, my):
                if click:
                    pygame.quit()
                    sys.exit()
        
        # implementing slideshow 
        if click:
            image_index = (image_index + 1) % len(um_images)
        image = pygame.image.load(f'{current_dir}/images/user_manual_images/{um_images[image_index]}')
        
        # window update
        pygame.display.flip()
        CLOCK.tick(60)
        SCREEN.blit(image, (0,0))
