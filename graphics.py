# Graphical User Interface for kAi

'''
Main file ran on application start

Contains all graphical user interfaces: menu, user manual and chat window
Imports AI responses from responses.py, which is trained using training.py
'''

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Imports

import os
import sys
import pygame
import datetime
import time
import win32api
import win32con
import win32gui
import responses

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Drawing Support Functions

def draw_rect_transparent(surface, colour, rect, radius):
    '''
    Draws transparent rectangles on given surface
    '''

    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA) # makes a surface from rectangles of given rectangles, with alpha property
    pygame.draw.rect(shape_surf, colour, shape_surf.get_rect(), border_radius=radius) # draws rectangle using surface
    surface.blit(shape_surf, rect)

def draw_centred_text(text, font, color, surface, x, y):
    '''
    Outputs text at the specified location, with (x,y) being the centre of the text object, using the required parameters
    '''

    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def draw_lefted_text(text, font, color, surface, x, y):
    '''
    Outputs text at the specified location, with (x,y) being the left centre of the text object, using the required parameters
    '''

    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.left = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Menu Support Functions

def notification_box_text(message_notif_s, message_notif_r, sent_notif_button, received_notif_button):
    '''
    Outputs notification toggle button text to indicate what the currently selected option is
    '''

    # message sent notification
    if message_notif_s:
        str_notif_s = 'ON'
    else:
        str_notif_s = 'OFF'
    draw_centred_text(f'Message Sent: {str_notif_s}', FONT_CB_20, (255, 255, 255), SCREEN, sent_notif_button.centerx, sent_notif_button.centery)
