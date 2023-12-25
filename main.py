import pygame
import numpy as np
import math


# SETTINGS #

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
FPS = 60

BACKGROUND_COLOR = [0, 0, 0]
LINE_COLOR = [0, 255, 0]

COPIES = 10
COPIES_DELTA = 20

############

size = 0.7
vtilt = 0
htilt = 0
voffset = 0
hoffset = 0
spin = 0
intencity = 1

speed = 200

parameters = []
for i in range(COPIES):
    parameters += [[0, 0, 0, 0, 0, 0, 0]]


pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()



def event_handler():
    #global
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()




def calc_corners(size, vtilt, htilt, voffset, hoffset, spin, intencity):
    


    top = (WINDOW_HEIGHT / 2) * (1-size) + voffset * WINDOW_HEIGHT
    bottom = WINDOW_HEIGHT - top + voffset * WINDOW_HEIGHT * 2
    left = (WINDOW_WIDTH / 2) * (1-size) + hoffset * WINDOW_WIDTH
    right = WINDOW_WIDTH - left + hoffset * WINDOW_WIDTH * 2

    return ([left + vtilt * WINDOW_WIDTH, top + htilt * WINDOW_HEIGHT],
    [right - vtilt * WINDOW_WIDTH, top - htilt * WINDOW_HEIGHT],
    [left - vtilt * WINDOW_HEIGHT, bottom - htilt * WINDOW_WIDTH],
    [right + vtilt * WINDOW_HEIGHT, bottom + htilt * WINDOW_WIDTH])


def calc_parameters(parameters, time, speed, copy_delta):
    for i in range(COPIES):
        time += copy_delta
        size = (time % speed) / speed
        voffset = (math.sin(time / 20)) / 50
        hoffset = (math.cos(time / 20)) / 50
        vtilt = ((math.sin(time / 20)) / 128) / (size*100 + 1)
        htilt = ((math.cos(time / 20)) / 128) / (size*100 + 1)
        spin = 0
        intencity = size
        parameters[i] = [size, voffset, hoffset, vtilt, htilt, spin, intencity]



def show():
    surface.fill(BACKGROUND_COLOR)

    for i in range(COPIES):
        left_top, right_top, left_bottom, right_bottom = calc_corners(*parameters[i])

        pygame.draw.line(surface, (0, 255 * parameters[i][-1], 0), left_top, left_bottom)
        pygame.draw.line(surface, (0, 255 * parameters[i][-1], 0), left_bottom, right_bottom)
        pygame.draw.line(surface, (0, 255 * parameters[i][-1], 0), right_bottom, right_top)
        pygame.draw.line(surface, (0, 255 * parameters[i][-1], 0), left_top, right_top)

    
    pygame.display.update()





if __name__ == "__main__":
    show()

    for i in range(100000000):
        event_handler()
        show()
        clock.tick(FPS)
        calc_parameters(parameters, i, speed, COPIES_DELTA)