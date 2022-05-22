import pygame
import random


class Particles():
    #model of particles
    def __init__(self, screen, x, y, size):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.color = (40, 43, 43) 
        self.thickness = 1
        

    def display_particle(self):
        #display a particle
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size, self.thickness)
