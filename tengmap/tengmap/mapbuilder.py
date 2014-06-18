#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()


if '__main__' == __name__:
    sw = 1500
    sh = 480
    screen = pygame.display.set_mode((sw, sh), 0, 32)
    clock = pygame.time.Clock()
    black = pygame.Color(0, 0, 0, 0)
    green = pygame.Color(0, 255, 0, 0)
    delta_x = 0
    delta_y = 0
    width = 32
    height = 32
    img = pygame.image.load('./pic/map.png').convert()
    indx = 0
    indy = 0
    vector = [{'x':0, 'y':1}, {'x':-1, 'y':0}, {'x':1, 'y':0}, {'x':0, 'y':-1}]
    kposy = {K_DOWN:0, K_LEFT:1, K_RIGHT:2, K_UP:3}
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                for key in kposy:
                    if key == event.key:
                        indx += vector[kposy[key]]['x']
                        indy += vector[kposy[key]]['y']
                        if indx < 0:
                            indx = 0
                        if indy < 0:
                            indy = 0
                        if indx >= 8:
                            indx = 7
                        if indy >= 112:
                            indy = 111
                        while delta_y * height + sh < indy * height + height:
                            delta_y += 1
                        while delta_y * height > indy * height:
                            delta_y -= 1
        pygame.draw.rect(screen, black, (0, 0, sw, sh))
        
        screen.blit(img, (-delta_x * width, -delta_y * height), (0, 0, img.get_width(), img.get_height()))
        pygame.draw.rect(screen, green, ((indx - delta_x)*width, (indy - delta_y) * height, width, height), 2)
        pygame.display.update()
        clock.tick(30)#fps 120