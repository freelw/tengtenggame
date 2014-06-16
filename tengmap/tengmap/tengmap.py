#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()

import json
import tenghero
import copy

class mapunit:
    def __init__(self, img_dir, indx, indy, width=32, height=32):
        self.img_dir = img_dir
        self.indx = indx
        self.indy = indy
        self.width = width
        self.height = height

    def setimg(self, img):
        self.img = img

    def display(self, delta_x, delta_y, screen):
        tx = self.mapx*self.width - delta_x
        ty = self.mapy*self.height - delta_y
        swidth = screen.get_width()
        sheight = screen.get_height()
        points = [{'x':tx,'y':ty},
                  {'x':tx+self.width,'y':ty},
                  {'x':tx,'y':ty+self.height},
                  {'x':tx+self.width,'y':ty+self.height}
                 ]
        for point in points:
            if delta_x <= point['x'] <= delta_x+swidth and delta_y <= point['y'] <= delta_y+sheight:
                break
        else:
            return
        screen.blit(self.img, (tx, ty), (self.indx*self.width, self.indy*self.height, self.width, self.height))

class tengmap:
    def __init__(self, info_dir='./mapinfo', r_dir_list = ['./pic/map.png']):
        self.info_dir = info_dir
        self.r_dir_list = r_dir_list
        self.imgs = self.loadImgs(self.r_dir_list)
        self.info = self.loadInfo(self.info_dir)

        self.unit_list = self.loadUnits(self.info['unit_list'])
        for unit in self.unit_list:
            unit.setimg(self.imgs[unit.img_dir])

        self.width_cnt = self.info['width_cnt']
        self.height_cnt = self.info['height_cnt']

        maparr = self.info['maparr']

        self._map =[[None for i in xrange(self.height_cnt)] for j in xrange(self.width_cnt)]
        for i in xrange(self.width_cnt):
            for j in xrange(self.height_cnt):
                self._map[i][j] = copy.copy(self.unit_list[maparr[i][j]])
                self._map[i][j].mapx = i
                self._map[i][j].mapy = j

        #for unit in self.unit_list:
        #    self._map[unit.mapx][unit.mapy] = copy.copy(unit)

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
        for item in ulist:
            unit = mapunit(**item)
            unit_list.append(unit)
        return unit_list

    def display(self, delta_x, delta_y, screen):
        for arr in self._map:
            for unit in arr:
                unit.display(delta_x, delta_y, screen)

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    clock = pygame.time.Clock()
    tmap = tengmap()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        tmap.display(0, 0, screen)
        pygame.display.update()
        clock.tick(1)#fps 120
