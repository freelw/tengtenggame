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
        self.blue = pygame.Color(0, 0, 255)
        self.white = pygame.Color(255, 255, 255)
        self.clock = pygame.time.Clock()
        self.font = None
        self.title_surface = None
        self.title_left = None
        self.msglock = False
        self.msg = None
        self.msg_surface = None
        
        self.prepair()
        
        
    def event_callback(self, event):
        raise tengException('not impl')
        
    def on_over(self):
        raise tengException('not impl')
        
    def prepair(self):
        raise tengException('not impl')
        
    def on_idle(self):
        raise tengException('not impl')
    
    def get_title(self):
        return 'title'
        
    def get_font(self):
        if self.font is None:
            self.font = pygame.font.SysFont("microsoftyahei", 16)
        return self.font

    def get_title_surface(self):
        if self.title_surface is None:
            self.title_surface = self.get_font().render(self.get_title(), True, (0, 0, 255))
        return self.title_surface
        
    def get_box_msg(self):
        return ''
        
    def check_K_RETURN(self, event):
        if event.type == KEYDOWN:
            if K_RETURN == event.key:
                if not self.msglock:
                    self.msgiter = self.get_box_msg()
                    self.msg = self.msgiter.next()
                    if '' != self.msg:
                        self.msglock = True
                        self.hero.speed = 0
                else:
                    self.msg = self.msgiter.next()
                    if '' == self.msg:
                        self.msg = ''
                        self.msglock = False
                    self.msg_surface = None

    def show_msg(self):
        pygame.draw.rect(self.screen, self.blue, (0 , 2./3 * self.screen.get_height(), self.screen.get_width(), self.screen.get_height()))
        pygame.draw.rect(self.screen, self.white, (0 , 2./3 * self.screen.get_height(), self.screen.get_width()-2, self.screen.get_height()-2), 2)
        if self.msg_surface is None:
            self.msg_surface = self.get_font().render(self.msg, True, (255, 255, 255))
        
        self.screen.blit(self.msg_surface, (5, 2./3 * self.screen.get_height() + 5))

    def display(self):
        while True:
            if self.over:
                return self.on_over()
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if not self.msglock:
                    self.tcm.event_callback(event)
                    self.event_callback(event)
                    
                self.check_K_RETURN(event)
                
            self.tcm.run()
            self.tcm.fixbyhero()
            pygame.draw.rect(self.screen, self.black, (0, 0, self.screen.get_width(), self.screen.get_height()))
            self.tcm.display(self.screen)
            self.screen.blit(self.get_title_surface(), ((self.screen.get_width() - self.get_title_surface().get_width())/2, 0))
            if self.msglock:
                self.show_msg()
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