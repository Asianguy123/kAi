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
