
import math
import pygame
import config as conf
import particles as partic
import random
import sys



def run_test():
    pygame.init()

    #Screen 
    super_settings = conf.Configuracion()
    screen = pygame.display.set_mode((super_settings.screen_widht, super_settings.screen_height))
    pygame.display.set_caption('Super test!')
    screen.fill(super_settings.bg_scolor)

    #Create n particles
    n_particles = 1
    particles_group = []
    for particle in range(n_particles):
        x = random.randint(50, 300) 
        y = random.randint(50, 300)
        size = random.randint(10, 25)
        particle = partic.Particles(screen, x , y, size)
        particle.speed = 0.01
        particle.angle = random.uniform(0, math.pi*2)
        particles_group.append(particle)

    def screen_on(screen):
        #Keeps screen on display
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
            screen.fill(super_settings.bg_scolor)

            #Display n particulas
            for particula in particles_group:
                    particula.move()
                    particula.display_particle()
            pygame.display.flip() #create a new display /erease last particle 
         
    screen_on(screen)#Call last function
    

run_test()