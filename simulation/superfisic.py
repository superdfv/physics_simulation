
import pygame
import config as conf
import functions as fun
import particles as partic


def run_test():
    pygame.init()
    #Pantalla
    super_settings = conf.Configuracion()
    screen = pygame.display.set_mode((super_settings.screen_widht, super_settings.screen_height))
    pygame.display.set_caption('Test')
    pygame.display.set_caption('Super test!')
    screen.fill(super_settings.bg_scolor)
    #Crea particula
    particle_uno = partic.Particles(screen, 100, 50, 15)
    particle_uno.display_particle()
    #Mantener pantalla on display 
    super_settings.screen_on()

    


run_test()