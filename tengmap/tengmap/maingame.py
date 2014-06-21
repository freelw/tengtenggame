#!/usr/bin/env python
#coding=utf-8
import pygame
from pygame.locals import *
pygame.init()
import tengscene

import gamescene1
import gamescene2
import gamescene3
import gamescene4
from sys import exit

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    
    scene2 = gamescene2.gamescene2(screen, './maps/scene2', './pic/153.png')
    scene1 = gamescene1.gamescene1(screen, './maps/scene1', './pic/153.png')
    scene3 = gamescene3.gamescene3(screen, './maps/scene3', './pic/153.png')
    scene4 = gamescene4.gamescene4(screen, './maps/scene4', './pic/153.png')
    scenedic = {'jitan':scene1,
            'shitang':scene2,
            'qinshi':scene3,
            'shitangli':scene4
    }
    nextscene = scene2
    while True:
        nextscene.setbegin()
        scenename = nextscene.display()
        if scenename is None:
            break
        nextscene = scenedic[scenename]