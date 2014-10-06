#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()
from tengException import tengException



class soldier:
    def __init__(self, dir, x, y):
        self.dir = dir
        self.img = pygame.image.load(self.dir).convert_alpha()
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def display(self, surface):
        surface.blit(self.img, (self.x, self.y), (0, 0, self.width, self.height)

class tengfight:
    def __init__(self):
        pass
    def display(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
    def get_heros(self):
        raise tengException('not impl')
    def get_monsters(self):
        raise tengException('not impl')
