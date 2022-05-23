import pygame
import random
import math





class Particles():
    #model of particles
    def __init__(self, screen, x, y, size):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.color = (231, 222, 234 ) 
        self.thickness = 0
        
        

    def display_particle(self):
        #display a particle
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size, self.thickness)
    

    def gravity(self):
        #gravity pull
        self.y = round(self.y + 0.5,2)

        

        
    