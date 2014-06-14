#!/usr/bin/env python
#coding=utf-8

import pygame
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
pygame.init()
#初始化pygame,为使用硬件做准备

import time
import math
import conf

class pic:
    def __init__(self, dic):
        print dic
        self.dir = dic['dir']
        self.fx = dic['fx']
        self.tx = dic['tx']
        self.fy = dic['fy']
        self.ty = dic['ty']
        self.timelen = dic['timelen']
        self.m_pic = pygame.image.load(self.dir).convert()
        self.curx = self.fx
        self.cury = self.fy
        self.color = pygame.Color(0, 0, 0, 0)

    def start(self, screen, bland_alpha_surface, msg_callback):
        self.starttime = time.time()
        while self.show(screen, bland_alpha_surface):
            msg_callback()
        
        
    def show(self, screen, bland_alpha_surface):
        
        screen.blit(self.m_pic, (self.curx, self.cury))
        now = time.time()
        tlen = now - self.starttime
        percentage = 1. * tlen / self.timelen
        self.curx = (self.tx - self.fx) * percentage + self.fx
        self.cury = (self.ty - self.fy) * percentage + self.fy
        self.color.a = 255 - abs(int(math.sin(percentage * math.pi) * 255))
        pygame.draw.rect(bland_alpha_surface, self.color, (0, 0, bland_alpha_surface.get_width(), bland_alpha_surface.get_height()))
        screen.blit(bland_alpha_surface, (0,0))
        pygame.display.update()
        if percentage >= 1:
            return False
        return True
        
class tengMovie:
    def __init__(self, conf, screen):
        self.piclist = []
        #conf 格式：
        #conf = {
        #   "piclist":[{"dir":"","fx":0,"tx":1,"fy":0,"ty":1,"timelen":10}]
        #}
        self.screen = screen
        piclist = conf['piclist']
        for item in piclist:
            tpic = pic(item)
            self.piclist.append(tpic)
            
        self.size = len(self.piclist)
        self.bland_alpha_surface = pygame.Surface((screen.get_width(), screen.get_height()), flags=SRCALPHA, depth=32)
        musicdir = conf['music']
        self.loop = conf['loop']
        self.bg_music = pygame.mixer.Sound(musicdir)

    def run(self):
        self.bg_music.play(-1)
        if -1 == self.loop:
            while True:
                self.run_impl()
        else:
            for i in xrange(self.loop):
                self.run_impl()

    def run_impl(self):
        for tpic in self.piclist:
            self.msg_callback()
            tpic.start(self.screen, self.bland_alpha_surface, self.msg_callback)

    def msg_callback(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    mv = tengMovie(conf.conf, screen)
    mv.run()