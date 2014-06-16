#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()

import tengmap
class tengCamera:
    def __init__(self, x, y, width=640, height=480):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def setmap(self, tmap):
        self.tmap = tmap

    def display(self, screen):
        
        
