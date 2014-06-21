#!/usr/bin/env python
#coding=utf-8
import pygame
from pygame.locals import *
pygame.init()
import tengscene

class gamescene2(tengscene.tengscene):
    def event_callback(self, event):
        pass
        
    def on_over(self):
        pass

    def prepair(self):
        self.hero.x = 300
        self.hero.y = 100
        self.tcm.x = 0
        self.tcm.y = 0
        
    def on_idle(self):
        if 0 == self.hero.x:
            self.hero.x = 1
            self.hero.speed = 0
            self.hero.direction = 2
            self.setover()
        

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    scene = gamescene2(screen, './maps/scene2', './pic/153.png')
    scene.display()
    