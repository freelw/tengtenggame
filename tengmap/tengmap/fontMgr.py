#!/usr/bin/env python
#coding=utf-8


import pygame
from pygame.locals import *
pygame.init()

class fontMgr:
    def __init__(self):
        self.font = pygame.font.Font("./fonts/wryh.ttf", 16)
    def get_font(self):
        return self.font
