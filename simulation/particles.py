import pygame
import random
import math
from config import Configuracion


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
        self.screen_size = Configuracion()
          

    def display_particle(self):
        #display a particle
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size, self.thickness)
    

    def move(self):
        #move particle 
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    
    def bounce(self):
        #calculate boundries
        if self.x > self.screen_size.screen_widht - self.size:
            self.x = 2 * (self.screen_size.screen_widht - self.size) - self.x
            self.angle = - self.angle
        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
        if self.y > self.screen_size.screen_height - self.size:
            self.y = 2 * (self.screen_size.screen_height- self.size) - self.y
            self.angle = math.pi - self.angle
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle

    