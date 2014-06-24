#!/usr/bin/env python
#coding=utf-8
import pygame
from pygame.locals import *
pygame.init()
import tengscene

class gamescene4(tengscene.tengscene):
    def event_callback(self, event):
        pass
        
    def on_over(self):
        return self.nextscene
        
    def prepair(self):
        self.hero.x = 18*32
        self.hero.y = 19*32-1
        self.hero.direction = 3
        self.tcm.x = 20*32 - self.screen.get_width()
        self.tcm.y = 20*32 - self.screen.get_height()
        self.nextscene = None
    
    def on_idle(self):
        if abs(18*32-self.hero.x) < 20 and 19*32 == self.hero.y:    
            self.hero.y = 19*32-1
            self.hero.direction = 1
            self.hero.speed = 0
            self.nextscene = 'shitang'
            self.setover()

    def get_title(self):
        return u"食堂"

    def get_box_msg(self):
        return u"好饿呀！！！"
if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    scene = gamescene4(screen, './maps/scene4', './pic/153.png')
    scene.display()
    