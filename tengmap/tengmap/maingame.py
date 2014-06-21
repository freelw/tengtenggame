#!/usr/bin/env python
#coding=utf-8
import pygame
from pygame.locals import *
pygame.init()
import tengscene

import gamescene1
import gamescene2
from sys import exit

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    scene2 = gamescene2.gamescene2(screen, './maps/scene2', './pic/153.png')
    scene1 = gamescene1.gamescene1(screen, './maps/scene1', './pic/153.png')
    while True:
        scene2.setbegin()
        scene2.display()
        scene1.setbegin()
        scene1.display()