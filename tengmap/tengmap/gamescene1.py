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
        return self.nextscene
        
    def prepair(self):
        self.hero.x = 320-32
        self.hero.y = 1248-1
        self.hero.direction = 3
        self.tcm.x = 0
        self.tcm.y = 1248+32-self.screen.get_height()
        self.nextscene = None
    
    def on_idle(self):
        if self.hero.y == 1248:
            self.hero.y = 1248-1
            self.hero.speed = 0
            self.hero.direction = 3
            self.nextscene = 'shitang'
            self.setover()
    def get_title(self):
        return u"祭坛"
        
    def get_box_msg(self):
        return u"这里就是传说中的祭坛吗。。。？"

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    scene = gamescene1(screen, './maps/scene1', './pic/153.png')
    scene.display()
    