#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()
from tengException import tengException
import fontMgr



class soldier:
    def __init__(self, dir, name, x, y, life, attack, defense, dx = 0, dy = 0, width = None, height = None):
        self.dir = dir
        self.name = name
        self.img = pygame.image.load(self.dir).convert_alpha()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.maxlife = life
        self.currentlife = life
        self.attack = attack
        self.defense = defense
        if width is None:
            self.width = self.img.get_width()
        else:
            self.width = width
        if height is None:
            self.height = self.img.get_height()
        else:
            self.height = height
        self.fontMgr = fontMgr.fontMgr()

    def get_blood(self):
        self.currentlife = self.maxlife

    def get_font(self):
        return self.fontMgr.get_font()

    def display(self, surface):
        detail = '%s/%s' % (self.maxlife, self.currentlife)
        msg_surface = self.get_font().render(detail, True, (255, 255, 255))
        surface.blit(msg_surface, (self.x + self.width/2, self.y - 20))
        surface.blit(self.img, (self.x, self.y), (self.dx, self.dy, self.width, self.height))

    def hit(self, enemy):
        enemy.currentlife -= max(self.attack-enemy.defense, 0)
        msg = u'%s attack %s %s hurt %s' % (self.name, enemy.name, enemy.name, max(self.attack-enemy.defense, 0))
        return msg
class tengfight:
    def __init__(self, surface):
        self.surface = surface
        self.black = pygame.Color(0, 0, 0, 0)
        self.blue = pygame.Color(0, 0, 255)
        self.white = pygame.Color(255, 255, 255)
        self.under_control = True
        self.fighting = self.fight()
        self.is_over = False
        self.fontMgr = fontMgr.fontMgr()

    def display(self):
        self.is_over = False
        self.hero.get_blood()
        self.monster.get_blood()
        while True:
            self.display_bg()
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                self.event_callback(event)
            self.check_win()
            hero = self.get_hero()
            hero.display(self.surface)
            monster = self.get_monster()
            monster.display(self.surface)
            pygame.display.update()
            if self.is_over:
                break

    def check_win(self):
        if self.monster.currentlife <= 0:
            self.draw_msg('you win')
            self.is_over = True

    def get_hero(self):
        raise tengException('not impl')
    def get_monster(self):
        raise tengException('not impl')
    def display_bg(self):
        swidth = self.surface.get_width()
        sheight = self.surface.get_height()
        pygame.draw.rect(self.surface, self.black, (0, 0, swidth, sheight))

    def fight(self):
        while True:
            yield 'your turn'
            yield self.hit_monster()
            yield 'enemy turn'
            yield self.monster_hit()
            
    def event_callback(self, event):
        if self.under_control:
            if event.type == KEYDOWN:
                if K_RETURN == event.key:
                    msg = self.fighting.next()
                    self.draw_msg(msg)

    def draw_msg(self, msg):
        pygame.draw.rect(self.surface, self.blue, (0 , 2./3 * self.surface.get_height(), self.surface.get_width(), self.surface.get_height()))
        pygame.draw.rect(self.surface, self.white, (0 , 2./3 * self.surface.get_height(), self.surface.get_width()-2, self.surface.get_height()-2), 2)
        msg_surface = self.get_font().render(msg, True, (255, 255, 255))
        self.surface.blit(msg_surface, (5, 2./3 * self.surface.get_height() + 5))

    def hit_monster(self):
        return self.hero.hit(self.monster)
    def monster_hit(self):
        return self.monster.hit(self.hero)
    def get_font(self):
        return self.fontMgr.get_font()
        
class testfight(tengfight):
    def __init__(self, surface):
        tengfight.__init__(self, surface)
        self.heros = []
        self.monsters = []
        hero1 = soldier('./pic/153.png', 90, 200, 0, 64, 32, 32)
        monster1 = soldier('./pic/12.png', 300, 80)
        self.heros.append(hero1)
        self.monsters.append(monster1)

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
