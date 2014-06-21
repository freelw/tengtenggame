#!/usr/bin/env python
#coding=utf-8
import pygame
from pygame.locals import *
pygame.init()
import tengscene

class gamescene3(tengscene.tengscene):
    def event_callback(self, event):
        pass
        
    def on_over(self):
        pass
        
    def prepair(self):
        self.hero.x = 0
        self.hero.y = 0
        self.hero.direction = 3
        self.tcm.x = 0
        self.tcm.y = 0
    
    def on_idle(self):
        pass

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    scene = gamescene3(screen, './maps/scene3', './pic/153.png')
    scene.display()
    