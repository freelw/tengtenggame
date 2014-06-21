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
        return self.nextscene
        
    def prepair(self):
        self.hero.x = 0
        self.hero.y = 1
        self.hero.direction = 3
        self.tcm.x = 0
        self.tcm.y = 0
        self.nextscene = None
    
    def on_idle(self):
        if 0 == self.hero.y:
            self.hero.y = 1
            self.hero.direction = 1
            self.hero.speed = 0
            self.nextscene = 'shitang'
            self.setover()
            

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    scene = gamescene3(screen, './maps/scene3', './pic/153.png')
    scene.display()
    