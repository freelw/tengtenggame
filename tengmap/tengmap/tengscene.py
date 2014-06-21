#!/usr/bin/env python
#coding=utf-8

import tengmap
import tenghero
import tengcamera

import pygame
from pygame.locals import *
pygame.init()
from sys import exit
import math

class tengException(Exception):
    def __self(self, log):
        Exception.__init__(self)
        self.msg = log

class tengscene:
    def __init__(self, screen, mapdir, herodir):
        self.screen = screen
        self.mapdir = mapdir
        self.herodir = herodir
        self.over = False
        self.tmap = tengmap.tengmap(self.mapdir)
        self.tcm = tengcamera.tengCamera(0, 0)
        self.tcm.setmap(self.tmap)
        self.hero = tenghero.tengHero(self.herodir)
        self.hero.setMapCheckFunc(self.tmap.isallow)
        self.tcm.bindhero(self.hero)
        self.black = pygame.Color(0, 0, 0, 0)
        self.clock = pygame.time.Clock()
        
        self.prepair()
        
    def event_callback(self, event):
        raise tengException('not impl')
        
    def on_over(self):
        raise tengException('not impl')
        
    def prepair(self):
        raise tengException('not impl')
        
    def on_idle(self):
        raise tengException('not impl')

    def display(self):
        while True:
            if self.over:
                return self.on_over()
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                self.tcm.event_callback(event)
                self.event_callback(event)
            self.tcm.run()
            self.tcm.fixbyhero()
            pygame.draw.rect(self.screen, self.black, (0, 0, self.screen.get_width(), self.screen.get_height()))
            self.tcm.display(self.screen)
            pygame.display.update()
            self.clock.tick(50)
            self.on_idle()

    def setover(self):
        self.over = True
    
    def setbegin(self):
        self.over = False
        
    def dis(self, x0, y0, x1, y1):
        lx = x1 - x0
        ly = y1 - y0
        return math.sqrt(lx**2+ly**2)