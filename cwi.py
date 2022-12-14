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
