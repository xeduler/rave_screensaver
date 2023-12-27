import pygame
import numpy as np
import math


# SETTINGS #

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
FPS = 60

BACKGROUND_COLOR = [0, 0, 0]
LINE_COLOR = [0, 255, 0]

speed = 252
COPIES = 11
COPIES_DELTA = speed / COPIES

############




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




def calc_corners(size, voffset, hoffset, vtilt, htilt, spin, intencity):
    width_size = WINDOW_WIDTH #* (1-size)
    height_size = WINDOW_HEIGHT# * (1-size)


    top = (WINDOW_HEIGHT / 2) * (1-size) + voffset * WINDOW_HEIGHT
    bottom = WINDOW_HEIGHT - top + voffset * WINDOW_HEIGHT * 2
    left = (WINDOW_WIDTH / 2) * (1-size) + hoffset * WINDOW_WIDTH
    right = WINDOW_WIDTH - left + hoffset * WINDOW_WIDTH * 2

    return ([left + vtilt * width_size, top + htilt * height_size],
    [right - vtilt * width_size, top - htilt * height_size],
    [left - vtilt * height_size, bottom - htilt * width_size],
    [right + vtilt * height_size, bottom + htilt * width_size])


def calc_parameters(parameters, time, speed, copy_delta):
    for i in range(COPIES):
        time += copy_delta
        size = ((time % speed) / speed)**2
        #size = (math.sin(time/speed)+2) / 3
        voffset = math.sin(time * 0.05) * 0.05
        hoffset = math.cos(time * 0.05) * 0.05
        vtilt = voffset / 6
        htilt = hoffset / 6
        spin = 0
        intencity = size
        parameters[i] = [size, voffset, hoffset, vtilt, htilt, spin, intencity]


#def shift_parameters(parameters, oversize=1.1):
#    if parameters[-1][0] > oversize


def show():
    surface.fill(BACKGROUND_COLOR)

    for i in range(COPIES):
        left_top, right_top, left_bottom, right_bottom = calc_corners(*parameters[i])

        pygame.draw.line(surface, (0, 255 * parameters[i][-1], 0), left_top, left_bottom, 4)
        pygame.draw.line(surface, (0, 255 * parameters[i][-1], 0), left_bottom, right_bottom, 4)
        pygame.draw.line(surface, (0, 255 * parameters[i][-1], 0), right_bottom, right_top, 4)
        pygame.draw.line(surface, (0, 255 * parameters[i][-1], 0), left_top, right_top, 4)

        #pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(*left_top, 100, 100))


    pygame.display.update()





if __name__ == "__main__":
    show()

    for i in range(100000000):
        event_handler()
        show()
        clock.tick(FPS)
        calc_parameters(parameters, i, speed, COPIES_DELTA)
        #shift_parameters(parameters, oversize=1.1)