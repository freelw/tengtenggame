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
        self.clock = pygame.time.Clock()
        self.boundx = 0
        self.boundy = 0
        self.fcheck = None
        self.lastkey = None

    def setbound(self, x, y):
        self.boundx = x
        self.boundy = y
        
    def setMapCheckFunc(self, fcheck):
        self.fcheck = fcheck
    

    def blit(self, surface, delta_x, delta_y):
        tx = self.state * self.width
        ty = self.direction * self.height
        #print 'hero : ', self.x, ' ', self.y, ' ', tx, ' ', ty, ' ', self.width, ' ', self.height
        surface.blit(self.img, (self.x - delta_x, self.y - delta_y), (tx, ty, self.width, self.height))

    def dis(self, x0, y0, x1, y1):
        lx = x1 - x0;
        ly = y1 - y0
        return math.sqrt(lx ** 2 + ly ** 2)

    def fix(self, x, y):
        x = min(x, self.boundx - self.width)
        y = min(y, self.boundy - self.height)
        x = max(0, x)
        y = max(0, y)
        
        if self.fcheck is not None:
            if not self.fcheck(self.x, self.y, x, y):
                return self.x, self.y
        return x, y

    def run(self):
        vctitem = self.vector[self.direction]
        if self.speed != 0:
            passedtime = self.clock.tick() / 1000.
            tx = self.x + vctitem['x'] * self.speed * passedtime
            ty = self.y + vctitem['y'] * self.speed * passedtime
            #self.x += vctitem['x'] * self.speed * passedtime
            #self.y += vctitem['y'] * self.speed * passedtime
            self.x, self.y = self.fix(tx, ty)
            if self.dis(self.change_state_x, self.change_state_y, self.x, self.y) > 10:
                self.change_state_x = self.x
                self.change_state_y = self.y
                self.state += 1
                self.state %= 4
        return 0 != self.speed

    def run_and_blit(self, surface, delta_x = 0, delta_y = 0):
        self.run()
        self.blit(surface, delta_x, delta_y)

    def event_callback(self, event):
        if event.type == KEYDOWN:
            for key in self.kposy.keys():
                if event.key == key:
                    self.lastkey = key
                    self.direction = self.kposy[key]
                    if 0 == self.speed:
                        self.clock.tick()
                    self.speed = 100
        elif event.type == KEYUP:
            for key in self.kposy:
                if event.key == key:
                    if self.lastkey == event.key:
                        self.speed = 0
                        break

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    hero = tengHero('./pic/153.png')
    hero.setbound(500, 500)
    black = pygame.Color(0, 0, 0, 0)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            hero.event_callback(event)
        pygame.draw.rect(screen, black, (0, 0, 640, 480))
        hero.run_and_blit(screen)
        pygame.display.update()
        clock.tick(50)#fps 120
