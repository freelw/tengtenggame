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
        self.clock = pygame.time.Clock()

    def run(self, screen):
        white = pygame.Color(0, 128, 255, 0)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit() 
                
                if event.type == KEYDOWN:
                    for key in self.kposy.keys():
                        if event.key == key:
                            ind = self.kposy[key]
                            
                            
                            tmp = self.x + self.width * self.vector[ind]['x']
                            if tmp >= 0 and tmp < self.img_width:
                                self.x = tmp
                            tmp = self.y + self.height * self.vector[ind]['y']
                            if tmp >= 0 and tmp < self.img_height:
                                self.y = tmp
                            
            print '%d %d %d %d ' % (self.x, self.y, self.width, self.height)
            pygame.draw.rect(screen, white, (0, 0, 640, 640))
            screen.blit(self.img, (0, 0), (self.x, self.y, self.width, self.height))
            pygame.display.update()
            self.clock.tick(10)
        
if '__main__' == __name__:
    screen = pygame.display.set_mode((200, 200), 0, 32)
    m = mapviewer('./pic/map.png')
    m.run(screen)