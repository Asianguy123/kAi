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
