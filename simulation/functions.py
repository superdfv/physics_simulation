import sys
import pygame


def check_keydown_events (event):
    #respond to keypress
    if event.key == pygame.K_q:
        #close game with ´q´
        sys.exit()