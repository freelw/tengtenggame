#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()

import tengmap
import tenghero
from sys import exit
class tengCamera:
    def __init__(self, x, y, width=640, height=480):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hero = None
        self.padding = 100

    def setmap(self, tmap):
        self.tmap = tmap

    def bindhero(self, hero):
        self.hero = hero
        self.hero.setbound(self.tmap.width, self.tmap.height)
        
    def allow_left(self, x):
        return x > 0
    def allow_right(self, x):
        return x + self.width < self.tmap.width
    def allow_top(self, y):
        return y > 0
    def allow_bottom(self, y):
        return y + self.height < self.tmap.height

    def fixbyhero(self):
        if self.hero is not None:
            if self.x > self.hero.x - self.padding:
                if self.allow_left(self.hero.x - self.padding):
                    self.x = self.hero.x - self.padding
            if self.x < self.hero.x + self.padding - self.width:
                if self.allow_right(self.hero.x + self.padding - self.width):
                    self.x = self.hero.x + self.padding - self.width
            if self.y > self.hero.y - self.padding:
                if self.allow_top(self.hero.y - self.padding):
                    self.y = self.hero.y - self.padding
            if self.y < self.hero.y + self.padding - self.height:
                if self.allow_bottom(self.hero.y + self.padding - self.height):
                    self.y = self.hero.y + self.padding - self.height

    def display(self, screen):
        self.tmap.display(screen, self.x, self.y)
        if self.hero is not None:
            self.hero.blit(screen, self.x, self.y)
        
    def event_callback(self, event):
        if self.hero is not None:
            self.hero.event_callback(event)
    def run(self):
        if self.hero is not None:
            self.hero.run()

        
if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    clock = pygame.time.Clock()
    tmap = tengmap.tengmap()
    tcm = tengCamera(0, 0)
    tcm.setmap(tmap)
    hero = tenghero.tengHero('./pic/153.png')
    hero.x = 320-32
    hero.y = 1248
    hero.setMapCheckFunc(tmap.isallow)
    tcm.x = 0
    tcm.y = 1248+32-screen.get_height()
    tcm.bindhero(hero)
    black = pygame.Color(0, 0, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            tcm.event_callback(event)
        tcm.run()
        tcm.fixbyhero()
        pygame.draw.rect(screen, black, (0, 0, 640, 480))
        tcm.display(screen)
        pygame.display.update()
        clock.tick(50)