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
# Support Functions

def draw_rect_transparent(surface, colour, rect):
    '''
    Draws transparent rectangles on given surface
    '''

    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA) # makes a surface from rectangles of given rectangles, with alpha property
    pygame.draw.rect(shape_surf, colour, shape_surf.get_rect()) # draws rectangle using surface
    surface.blit(shape_surf, rect)

def draw_centred_text(text, font, color, surface, x, y):
    '''
    Outputs text at the specified location, with (x,y) being the centre of the text object, using the required parameters
    '''

    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def notification_box_text(message_notif_s, message_notif_r, sent_notif_button, received_notif_button):
    '''
    Outputs notification toggle button text to indicate what the currently selected option is
    '''

    # message sent notification
    if message_notif_s:
        str_notif_s = 'ON'
    else:
        str_notif_s = 'OFF'
    draw_centred_text(f'Message Sent: {str_notif_s}', font_s, (255, 255, 255), SCREEN, sent_notif_button.centerx, sent_notif_button.centery)

    # message received notification
    if message_notif_r:
        str_notif_r = 'ON'
    else:
        str_notif_r = 'OFF'
    draw_centred_text(f'Message Received: {str_notif_r}', font_r, (255, 255, 255), SCREEN, received_notif_button.centerx, received_notif_button.centery)

# ---------------------------------------------------------------------------------------------------------------------
# Main Function

def main():
    '''
    Main function for the main menu, runs and display menu screen
    Calls other screens, dependent on user action
    '''

    # booleans
    click = False
    message_notif_s = True
    message_notif_r = True

    # click boxes
    quit_icon = pygame.Rect(891, 7, 24, 24)
    chat_button = pygame.Rect(542, 366, 192, 58)
    help_button = pygame.Rect(542, 454, 192, 58)
    sent_notif_button= pygame.Rect(542, 541, 192, 58)
    received_notif_button = pygame.Rect(542, 628, 192, 58)
    hover_boxes = [chat_button, help_button, sent_notif_button, received_notif_button]

    while True:
        mx, my = pygame.mouse.get_pos()

        # ---------------------------------------------------------------------------------------------------------------------
        # Drawing Items

        draw_rect_transparent(SCREEN, (0, 0, 0, 0), quit_icon)
        draw_rect_transparent(SCREEN, (0, 0, 0, 0), chat_button)
        draw_rect_transparent(SCREEN, (0, 0, 0, 0), help_button)
        draw_rect_transparent(SCREEN, (0, 0, 0, 0), sent_notif_button)
        draw_rect_transparent(SCREEN, (0, 0, 0, 0), received_notif_button)
        notification_box_text(message_notif_s, message_notif_r, sent_notif_button, received_notif_button)

        # box hover outline
        for box in hover_boxes:
            if box.collidepoint(mx, my):
                pygame.draw.rect(SCREEN, (0, 184, 252), box, 4)
   
        # ---------------------------------------------------------------------------------------------------------------------
        # Event Loop

        click = False
        for event in pygame.event.get():    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # ---------------------------------------------------------------------------------------------------------------------
        # Clicks

        if click:
            # help button icon click detection
            help_icon_region = (mx - (354 + 22))**2 + ((my - 19)**2)
            if help_icon_region <= 256 or help_button.collidepoint(mx, my):
                user_manual.um_main()
    
            # quit button icon click detection
            if quit_icon.collidepoint(mx, my):
                pygame.quit()
                sys.exit()
            
            # chat button click detection, send to chat window
            if chat_button.collidepoint(mx, my):
                cwi.chat_window()
        
            # notification toggle click detection
            if sent_notif_button.collidepoint(mx, my):
                message_notif_s = not message_notif_s
            if received_notif_button.collidepoint(mx, my):
                message_notif_r = not message_notif_r

        # window update
        pygame.display.flip()
        CLOCK.tick(60)
        SCREEN.fill(transparent)
        SCREEN.blit(bg_image, (354,0))
