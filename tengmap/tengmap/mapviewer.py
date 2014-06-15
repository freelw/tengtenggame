#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()

class mapviewer:
    def __init__(self, dir, width = 32, height = 32, x = 0, y = 0):
        self.dir = dir
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.img = pygame.image.load(self.dir).convert()
        self.vector = [{'x':0, 'y':1}, {'x':-1, 'y':0}, {'x':1, 'y':0}, {'x':0, 'y':-1}]
        self.kposy = {K_DOWN:0, K_LEFT:1, K_RIGHT:2, K_UP:3}
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

    def run(self):
        screen = pygame.display.set_mode((640, 480), 0, 32)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit() 
                
                if event.type = KEYDOWN:
                    for key in self.kposy.keys()
                        if evnet.key == key:
                            ind = self.kposy[key]
                            if self.x + self.width < self.img_width:
                                self.x += self.width * self.vector[ind]
                            if self.y + self.heght <  self.img_height:
                                self.y += self.heght * self.vector[ind]
        
if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    m = mapviewer('./pic/