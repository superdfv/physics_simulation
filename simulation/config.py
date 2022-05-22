import pygame
import sys

class Configuracion():
    #store all settings for test
    def __init__(self):
        #screen settings
        self.screen_widht = 400
        self.screen_height = 400
        self.bg_scolor = (196, 242, 252)
    
    def screen_on(self):
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    #close game with ´q´
                    if event.key == pygame.K_q:
                         sys.exit()