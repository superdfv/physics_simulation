import pygame


class Particles():
    #model of particles
    def __init__(self, screen, x, y, size):
        self.x = x 
        self.y = y
        self.size = size
        self.color = (40, 43, 43) 
        self.thickness = 1
        self.screen = screen

    def display_particle(self):
        #display a particle
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size, self.thickness)
