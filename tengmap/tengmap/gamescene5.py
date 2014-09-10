#!/usr/bin/env python
#coding=utf-8
import pygame
from pygame.locals import *
pygame.init()
import tengscene

class gamescene5(tengscene.tengscene):
    def event_callback(self, event):
        pass
        
    def on_over(self):
        return self.nextscene
        
    def prepair(self):
        self.hero.x = 320
        self.hero.y = 350-1
        self.hero.direction = 3
        self.tcm.x = 0
        self.tcm.y = 0
        self.nextscene = None
    
    def on_idle(self):
        if 350 <= self.hero.y:
            self.hero.x = 320
            self.hero.y = 350-1
            self.hero.direction = 3
            self.hero.speed = 0
            self.tcm.x = 0
            self.tcm.y = 0
            self.nextscene = 'qinshi'
            self.setover()

    def get_title(self):
        return u"寝室二楼"
    
    def shallchat1(self):
        print self.hero.x, self.hero.y
        return self.hero.x >= 320 and self.hero.x <=350 and self.hero.y <= 256 and self.hero.y >= 220   
        
    def get_box_msg(self):
        if self.shallchat1():
            yield u'恭喜你来到LW的世界！！！！'
            yield u'这里是LW世界的第一关，我是第一个线索！'
            yield u'找到祭坛以通关！'
            yield u'出发吧少年！'
            yield ''
        yield u"DDDDDDota!!!!!"
        yield ''

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    scene = gamescene5(screen, './maps/scene5', './pic/153.png')
    scene.display()
    