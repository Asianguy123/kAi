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
import menu
import user_manual

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main Function

def chat_window(notif_s, notif_r):

    # setup
    CWSCREEN = menu.SCREEN
    CWCLOCK = menu.CLOCK
    CWMESSAGE_SIZE = 24
    current_dir = os.getcwd()
