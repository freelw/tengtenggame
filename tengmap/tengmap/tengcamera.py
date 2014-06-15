#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()

class tengCamera:
    def __init__(self, x, y, width=640, height=480):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
    def display(self):
        
        
