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
        surface.blit(self.img, (self.x, self.y), (0, 0, self.width, self.height))

class tengfight:
    def __init__(self, surface):
        self.surface = surface

    def display(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            for hero in self.get_heros():
                hero.display(self.surface)
            for monster in self.get_monsters():
                monster.display(self.surface)
            pygame.display.update()

    def get_heros(self):
        raise tengException('not impl')
    def get_monsters(self):
        raise tengException('not impl')
    def get_bg(self):
        raise tengException('not impl')

class testfight(tengfight):
    def __init__(self, surface):
        tengfight.__init__(self, surface)
        self.heros = []
        self.monsters = []
        hero1 = soldier('./pic/12.png', 0, 0)
        self.heros.append(hero1)

    def get_heros(self):
        return self.heros
    def get_monsters(self):
        return self.monsters
    def get_bg(self):
        pass

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    black = pygame.Color(0, 0, 0, 0)
    clock = pygame.time.Clock()


    fight = testfight(screen)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        pygame.draw.rect(screen, black, (0, 0, 640, 480))
        fight.display()
        pygame.display.update()
        clock.tick(50)#fps 120
