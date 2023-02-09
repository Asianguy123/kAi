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

    # message received notification
    if message_notif_r:
        str_notif_r = 'ON'
    else:
        str_notif_r = 'OFF'
    draw_centred_text(f'Message Received: {str_notif_r}', FONT_CB_18, (255, 255, 255), SCREEN, received_notif_button.centerx, received_notif_button.centery)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chat Window Support Functions

def get_time():
    '''
    Gets current device time in 24 hour using the datetime module
    '''

    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime('%H:%M') # formats to 24 hour
    return timestamp

def box_hover(surface, button, selected_button, hover):
    '''
    Draws an outline box to the hovered upon box, or the currently selected box
    '''

    if hover:
        pygame.draw.rect(surface, (0, 184, 252), button, 4, border_radius=6)
    pygame.draw.rect(surface, (0, 184, 252), selected_button, 4, border_radius=6)

# ---------------------------------------------------------------------------------------------------------------------
# Message Functions

def message_split(font, message, max_length):
    '''
    Splits the user input message into message lines that can be displayed in one message block
        - prevents messages covering the whole screen, and allows for paragraphing
    '''

    tokenised_message = message.split(' ')
    messages = []
    text = ''
    for i in tokenised_message:
        # if the input has word longer than the message width, split it
        if font.size(i)[0] > (max_length - 5):
            for chr in i:
                if font.size(text)[0] > (max_length - 5):
                    messages.append(text)
                    text = ''
                else:
                    text += chr
        
        else:
            # checks if message line is within maximum message bubble width size
            if font.size(text + i + ' ')[0] < (max_length - 5):
                text += i + ' '
            else:
                messages.append(text)
                text = i + ' '
    messages.append(text.rstrip()) # removing last space
    return messages

def draw_messages(thread, font, font_size, time_font, topic_font, screen):
    '''
    Draws most recent messages that fit in the window
        - draws bubbles of an appropriate size for each message
        - spaces the bubbles accordingly
        - outputs time of message next to bubble
        - draws indicator of topic change
    '''

    y = 590 # bottom of lowest possible bubble
    for i in thread:
        if i[0] == 2:
            if (y - topic_font.size(i[1])[1]) > 70:
                draw_centred_text(i[1], topic_font, (0, 184, 252), screen, 731, y - 20)
            y -= 50
        else:
            bubble_height = int((len(i[1]) + 1) * (font_size))
            bubble_width = 0
