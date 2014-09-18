#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()



class soldier:
    def __init__(self, dir):
        self.dir = dir
        self.img = pygame.image.load(self.dir).convert_alpha()
        self.
class tengfight:
    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster
        