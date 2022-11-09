# Main Menu Window

'''
Start-up file
Menu interface - has sound options + advance to chat session
'''

# ---------------------------------------------------------------------------------------------------------------------
# Imports

import os
import sys
import pygame

# ---------------------------------------------------------------------------------------------------------------------
# Main Function

def main():
    click = False
    while True:
        
        mx, my = pygame.mouse.get_pos() 
       
        # event loop
        click = False
        for event in pygame.event.get():    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        # window update
        pygame.display.flip()
        CLOCK.tick(60)
        SCREEN.blit(bg_image, (0,0))
