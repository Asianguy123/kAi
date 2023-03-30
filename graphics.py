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

            # assigning bubble width based on message line lengths
            for line in i[1]:
                if font.size(line)[0] > bubble_width:
                    bubble_width = font.size(line)[0] + 20
            
            # setting user messages to right, ai responses to the left
            if i[0] == 1:
                x = 258
                time_x = x + bubble_width + 10
            else:
                x = 1204 - bubble_width
                time_x = x - 40
            
            # outputting text and if within most recent messages
            if (y - bubble_height) > 70:
                bubble = pygame.Rect(x, y - bubble_height, bubble_width, bubble_height)
                pygame.draw.rect(screen, (38, 38, 38), bubble, border_radius=15)
                for j, line in enumerate(reversed(i[1])):
                    draw_lefted_text(line, font, (255, 255, 255), screen, bubble.left + 10, y - (j + 1) * (bubble_height / (len(i[1]) + 1)))
                draw_lefted_text(i[2], time_font, (217, 217, 217), screen, time_x, bubble.centery)
                y -= (bubble_height + 10)
            else:
                return

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chat Window Function

def chat_window(notif_s, notif_r):
    '''
    Chat window - the main interface
    - takes in user string input and outputs an AI selected response
    - can switch between specific topics via the select buttons on the left
    ''' 

    # booleans, lists and text
    message_lines_list = []
    responses_lines_list = []
    message_thread = []
    click = False
    hover = False
    typing_active = False
    message_limit = False
    text = ''
    pretext = 'Send kAi a message'

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
    corpus_topics = ['general', 'anime', 'kpop', 'films', 'games', 'football', 'life', 'day', 'school']
    selected_topic_index = 0

    # message box
    message_box = pygame.Rect(275, 625, 875, 50)

    while True:
        mx, my = pygame.mouse.get_pos()
        hover = False
        hover_button = ''

        # ---------------------------------------------------------------------------------------------------------------------
        # Drawing Items

        draw_rect_transparent(SCREEN, (0, 0, 0, 0), home_icon, 0)
        draw_rect_transparent(SCREEN, (0, 0, 0, 0), quit_icon, 0)
        draw_rect_transparent(SCREEN, (0, 0, 0, 0), send_icon, 0)
        draw_rect_transparent(SCREEN, (0, 0, 0, 0), message_box, 0)
        for button in topic_buttons:
            draw_rect_transparent(SCREEN, (0, 0, 0, 0), button, 4)
            if button.collidepoint(mx, my):
                hover = True
                hover_button = button
        box_hover(SCREEN, hover_button, topic_buttons[selected_topic_index], hover)
        draw_lefted_text(text, FONT_CB_20, (255, 255, 255), SCREEN, message_box.left, message_box.centery)
        draw_lefted_text(pretext, FONT_CI_20, (133, 133, 133), SCREEN, message_box.left, message_box.centery)
        draw_messages(reversed(message_thread), FONT_CB_MESSAGE, CWMESSAGE_SIZE, FONT_CB_14, FONT_CBI_TOPIC,SCREEN)

        # text input limit display
        if message_limit:
            draw_lefted_text('Message length limit reached!', FONT_CB_14, (0, 184, 252), SCREEN, message_box.left, message_box.bottom + 8)

        # ---------------------------------------------------------------------------------------------------------------------
        # Getting AI response

        if message_thread:
            if message_thread[-1][0] == 0:
                # time delay between notifs
                loop = True
                start_time = time.time()
                while loop:
                    end_time = time.time()
                    if (end_time - start_time) > 0.3:
                        loop = False
                
                # getting ai response to add to thread
                param_text = ' '.join(i for i in message_thread[-1][1])
                ai_response = responses.responses_main(corpus_topics[selected_topic_index], param_text)
                if type(ai_response) == list:
                    for i in ai_response:
                        responses_lines_list = message_split(FONT_CB_20, i, MAX_BUBBLE_LENGTH)
                        message_thread.append([1, responses_lines_list, get_time()])
                else:
                    responses_lines_list = message_split(FONT_CB_20, ai_response, MAX_BUBBLE_LENGTH)
                    message_thread.append([1, responses_lines_list, get_time()])            
                if notif_r:
                    pygame.mixer.Sound.play(MESSAGE_R_NOTIF)

        # ---------------------------------------------------------------------------------------------------------------------
        # Event Loop

        click = False
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
            # user message input
            if typing_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1] # deleting last character
                        message_limit = False
                    elif event.key == pygame.K_RETURN:
                        if text: # checking if there is a message to send
                            message_lines_list = message_split(FONT_CB_20, text, MAX_BUBBLE_LENGTH)
                            message_thread.append([0, message_lines_list, get_time()]) # 0 = user message and 1 = AI message, adds time of message
                            if notif_s:
                                pygame.mixer.Sound.play(MESSAGE_S_NOTIF)
                            text = ''
                    else:
                        # adding character if there is space in the message box
                        if not message_limit:
                            text += event.unicode
            
        if FONT_CB_20.size(text)[0] < (message_box.width - 5):
            message_limit = False
        else:
            message_limit = True

        # ---------------------------------------------------------------------------------------------------------------------
        # Clicks

        if click:
            # help button icon click detection
            help_icon_region = ((mx - 62)**2) + ((my - 19)**2)
            if help_icon_region <= 169:
                um_main()
            
            # home button icon click detection
            if home_icon.collidepoint(mx, my):
                menu()
            
            # quit button icon click detection
            if quit_icon.collidepoint(mx, my):
                pygame.quit()
                sys.exit()
                
            # send button icon click detection    
            if send_icon.collidepoint(mx, my):
                # same code as under ENTER key press
                if text:
                    message_lines_list = message_split(FONT_CB_20, text, MAX_BUBBLE_LENGTH)
                    message_thread.append([0, message_lines_list, get_time()])
                    if notif_s:
                        pygame.mixer.Sound.play(MESSAGE_S_NOTIF)
                    text = ''
            
            # message input box click detection
            if message_box.collidepoint(mx, my):
                typing_active = True
                pretext = ''

            # topic button click detection
            for i in range(len(topic_buttons)):
                if topic_buttons[i].collidepoint(mx, my):
                    selected_topic_index = i
                    message_thread.append([2, topic_strs[selected_topic_index], get_time()])
        
        # window update
        pygame.display.update()
        CLOCK.tick(30)
        SCREEN.blit(CW_BG_IMAGE, (0,0))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# User Manual Function

def um_main():
    '''
    - Runs the user manual, displays a slideshow of images that loops
    - Has special case buttons that work on a specific slide (slide 0)
    - Can be exited to return to main menu at any point by pressing the ESC key
    - Can be accessed from both the menu and chat window
    '''

    # setup
    click = False
    running = True
    image_index = 0
    
    # click boxes
    home_icon = pygame.Rect(10, 7, 27, 24)
    quit_icon = pygame.Rect(1249, 7, 23, 23)

    while running:
        mx, my = pygame.mouse.get_pos()

        # drawing click boxes
        draw_rect_transparent(SCREEN, (0, 0, 0, 0), home_icon, 0)
        draw_rect_transparent(SCREEN, (0, 0, 0, 0), quit_icon, 0)

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
