#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()

import math

class tengHero:
    def __init__(self, dir, x=0, y=0, width=32, height=32, speed = 0, direction=0, state=0):
        self.dir = dir
        self.img = pygame.image.load(self.dir).convert_alpha()
        self.x = x
        self.y = y
        self.change_state_x = self.x
        self.change_state_y = self.y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = direction
        self.state = state

        self.vector = [{'x':0, 'y':1}, {'x':-1, 'y':0}, {'x':1, 'y':0}, {'x':0, 'y':-1}]
        self.kposy = {K_DOWN:0, K_LEFT:1, K_RIGHT:2, K_UP:3}

    def blit(self, surface):
        tx = self.state * self.width
        ty = self.direction * self.height
        #print self.x, ' ', self.y, ' ', tx, ' ', ty, ' ', self.width, ' ', self.height
        surface.blit(self.img, (self.x, self.y), (tx, ty, self.width, self.height))
    def dis(self, x0, y0, x1, y1):
        lx = x1 - x0;
        ly = y1 - y0
        return math.sqrt(lx ** 2 + ly ** 2)

    def run(self):
        vctitem = self.vector[self.direction]
        if self.speed != 0:
            self.x += vctitem['x'] * self.speed
            self.y += vctitem['y'] * self.speed
            if self.dis(self.change_state_x, self.change_state_y, self.x, self.y) > 10:
                self.change_state_x = self.x
                self.change_state_y = self.y
                self.state += 1
                self.state %= 4

    def run_and_blit(self, surface):
        self.run()
        self.blit(surface)

    def event_callback(self, event):
        if event.type == KEYDOWN:
            for key in self.kposy.keys():
                if event.key == key:
                    self.direction = self.kposy[key]
                    self.speed = 1
        elif event.type == KEYUP:
            for key in self.kposy:
                if event.key == key:
                    self.speed = 0
                    break

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    hero = tengHero('./pic/153.png')
    black = pygame.Color(0, 0, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            hero.event_callback(event)
        pygame.draw.rect(screen, black, (0, 0, 640, 480))
        hero.run_and_blit(screen)
        pygame.display.update()
