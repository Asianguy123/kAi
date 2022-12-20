# Chat Window Interface

'''
The Main User Interface, where the chat session occurs
Output responses.py is fed into this file and outputted
'''

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Imports

import os
import sys
import pygame
import datetime
import menu
import user_manual

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Drawing Support Functions

def draw_rect_transparent(surface, colour, rect, radius):
    '''
    Draws transparent rectangles on given surface
    '''

    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA) # makes a surface from rectangles of given rectangles, with alpha property
    pygame.draw.rect(shape_surf, colour, shape_surf.get_rect(), border_radius=radius) # draws rectangle using surface
    surface.blit(shape_surf, rect)

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
# Chat Window Support Functions

def get_time():
    '''
    Gets current device time in 24 hour using the datetime module
    '''

    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime('%H:%M') # formats to 24 hour
    return timestamp

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
        

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main Function

def chat_window(notif_s, notif_r):

    # setup
    CWSCREEN = menu.SCREEN
    CWCLOCK = menu.CLOCK
    CWMESSAGE_SIZE = 24
    MAX_BUBBLE_LENGTH = 300
    current_dir = os.getcwd()
    bg_image = pygame.image.load(f'{current_dir}/images/cwindow.tif')
    font_message_box = pygame.font.SysFont('Calibri', 20, bold=True)
    small_font = pygame.font.SysFont('Calibri', 14, bold=True)
    font_messages = pygame.font.SysFont('Calibri', CWMESSAGE_SIZE, bold=True)
    topic_font = pygame.font.SysFont('Calibri', CWMESSAGE_SIZE - 4, bold=True, italic=True)
    message_s_notif = pygame.mixer.Sound(f'{current_dir}/notifications/message_sent.mp3')
    message_r_notif = pygame.mixer.Sound(f'{current_dir}/notifications/message_received.mp3')

    # toggles. lists and text
    message_lines_list = []
    responses_lines_list = []
    message_thread = []
    click = False
    hover = False
    typing_active = False
    message_limit = False
    text = ''      
    
    # icons
    home_icon = pygame.Rect(10, 7, 27, 24)
    quit_icon = pygame.Rect(1249, 7, 23, 23)
    send_icon = pygame.Rect(1160, 636, 30, 27)

    # topic buttons
    topic_buttons = [
        pygame.Rect(49, 87, 143, 46),
        pygame.Rect(49, 153, 143, 46),
        pygame.Rect(49, 219, 143, 46),
        pygame.Rect(49, 285, 143, 46),
        pygame.Rect(49, 351, 143, 46),
        pygame.Rect(49, 417, 143, 46),
        pygame.Rect(49, 483, 143, 46),
        pygame.Rect(49, 549, 143, 46),
        pygame.Rect(49, 615, 143, 46)
    ]
    topic_strs = ['General Chat', 'Anime', 'Kpop', 'Films', 'Games', 'Football', 'Your life', 'Your day', 'School']
    corpus_topics = ['general', 'anime', 'kpop', 'films', 'game', 'football', 'life', 'day', 'school']
    selected_topic_index = 0
