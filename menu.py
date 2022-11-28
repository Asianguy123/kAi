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
# Main Function

def main():
    '''
    Main function for the main menu, runs and display menu screen
    Calls other screens, dependent on user action
    '''
    pass

# ---------------------------------------------------------------------------------------------------------------------
# Setup

pygame.init()
CLOCK = pygame.time.Clock()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720 
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
current_dir = os.getcwd()
bg_image = pygame.image.load(f'{current_dir}/images/main_menu.tif')
font_s = pygame.font.SysFont('Calibri', 20, bold=True)
font_r = pygame.font.SysFont('Calibri', 18, bold=True)

# making the empty background transparent
transparent = (255, 0, 0)
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparent), 0, win32con.LWA_COLORKEY)

# ---------------------------------------------------------------------------------------------------------------------
# Runs Code

if __name__ == '__main__':
    main()
