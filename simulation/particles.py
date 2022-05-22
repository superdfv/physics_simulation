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
        self.color = (40, 43, 43) 
        self.thickness = 1
        self.speed = 0
        self.angle = 0
        
        

    def display_particle(self):
        #display a particle
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size, self.thickness)
    

    def move(self):
        #move particle 
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

