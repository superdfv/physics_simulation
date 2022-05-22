
import pygame
import config as conf
import particles as partic
import random



def run_test():
    pygame.init()
    #Pantalla
    super_settings = conf.Configuracion()
    screen = pygame.display.set_mode((super_settings.screen_widht, super_settings.screen_height))
    pygame.display.set_caption('Super test!')
    screen.fill(super_settings.bg_scolor)
    #Crea n particualas
    n_particles = 6
    particles_group = []
    for particle in range(n_particles):
        x = random.randint(50, 300) 
        y = random.randrange(50, 300, 20) 
        size = random.randint(10, 25)
        particle = partic.Particles(screen, x , y, size)
        particles_group.append(particle)
    #display n particulas
    for particula in particles_group:
         particula.display_particle()
         
    
    #Mantener pantalla on display 
    super_settings.screen_on()

    


run_test()