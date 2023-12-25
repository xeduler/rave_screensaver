import pygame
import numpy as np


# SETTINGS #

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
FPS = 60

BACKGROUND_COLOR = [255, 255, 255]

############


pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()



def event_handler():
    #global
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()




def show():
    surface.fill(BACKGROUND_COLOR)
    
    
    pygame.display.update()





if __name__ == "__main__":
    show()

    while 1:
        event_handler()
        show()
        clock.tick(FPS)