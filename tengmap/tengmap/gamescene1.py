#!/usr/bin/env python
#coding=utf-8
import pygame
from pygame.locals import *
pygame.init()
import tengscene

class gamescene1(tengscene.tengscene):
    def event_callback(self, event):
        pass
        
    def on_over(self):
        pass
        
    def prepair(self):
        self.hero.x = 320-32
        self.hero.y = 1248-1
        self.hero.direction = 3
        self.tcm.x = 0
        self.tcm.y = 1248+32-self.screen.get_height()
    
    def on_idle(self):
        if self.hero.y == 1248:
            self.hero.y = 1248-1
            self.hero.speed = 0
            self.hero.direction = 3
            self.setover()

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    scene = gamescene1(screen, './maps/scene1', './pic/153.png')
    scene.display()
    