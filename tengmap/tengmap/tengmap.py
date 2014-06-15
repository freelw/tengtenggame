#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()

import json
import tenghero

class mapunit:
    def __init__(self, img_dir, indx, indy, width=32, height=32):
        self.img_dir = img_dir
        self.indx = indx
        self.indy = indy
        self.width = width
        self.height = height

class tengmap:
    def __init__(self, info_dir, r_dir_list):
        self.info_dir = info_dir
        self.r_dir_list = r_dir_list
        self.imgs = self.loadImgs(self.r_dir_list)
        self.info = self.loadInfo(self.info_dir)

        self.default_unit = mapunit(**self.info['default_unit'])
        self.unit_list = self.loadUnits(self.info['unit_list'])
        self.width = self.info['width']
        self.height = self.info['height']
        self.camera_x = self.info['camera_x']
        self.camera_y = self.info['camera_y']
        self.camera_width = self.info['camera_width']
        self.camera_height = self.info['camera_height']
        self.hero = tenghero.tengHero(self.info['hero'])

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

    def loadUnits(self, ulist):
        unit_list = []
        for item in ulist
            unit = mapunit(**item)
            unit_list.append(unit)
        return unit_list
