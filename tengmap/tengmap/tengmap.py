#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()

import json

class mapunit:
    def __init__(self, img, x, y, width=32, height=32):
        self.img = img
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
class tengmap:
    def __init__(self, info_dir, r_dir_list):
        self.info_dir = info_dir
        self.r_dir_list = r_dir_list
        self.imgs = self.loadImgs(self.r_dir_list)
        self.info = self.loadInfo(self.info_dir)
        
        

    def loadImgs(self, r_dir_list):
        imgs = {}
        for dir in r_dir_list:
            img = pygame.image.load(dir).convert()
            imgs[dir] = img
        return imgs
        
    def loadInfo(self, dir):
        try:
            f = open(dir)
            content = ''
            for line in f:
                content += line
            f.close()
            return json.loads(content)
        except Exception, e:
            print 'loadInfo error %s' % e