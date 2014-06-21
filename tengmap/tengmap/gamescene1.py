#!/usr/bin/env python
#coding=utf-8
import pygame
from pygame.locals import *
pygame.init()
import tengscene

class gamescene1(tengscene.tengscene):
    def event_callback(self, event):
        print 'gamescene1'
        
    def on_over(self):
        print 'on_over'
        
    def prepair(self):
        self.hero.x = 320-32
        self.hero.y = 1248
        self.tcm.x = 0
        self.tcm.y = 1248+32-screen.get_height()

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    scene = gamescene1(screen, './maps/scene1', './pic/153.png')
    scene.display()
    