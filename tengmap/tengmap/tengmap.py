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

    def display(self, screen, delta_x, delta_y):
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
            if 0 <= point['x'] <= swidth and 0 <= point['y'] <= sheight:
                break
        else:
            return
        screen.blit(self.img, (tx, ty), (self.indx*self.width, self.indy*self.height, self.width, self.height))
        #if self.indx_sec is not None:
        #    screen.blit(self.img, (tx, ty), (self.indx_sec*self.width, self.indy_sec*self.height, self.width, self.height))

class tengmap:
    def __init__(self, info_dir='./mapinfo', r_dir_list = ['./pic/map.png']):
        self.info_dir = info_dir
        self.r_dir_list = r_dir_list
        self.imgs = self.loadImgs(self.r_dir_list)
        self.info = self.loadInfo(self.info_dir)
        down = self.info['down']
        up = self.info['up']

        self.unit_list = self.loadUnits(down['unit_list'])
        for unit in self.unit_list:
            unit.setimg(self.imgs[unit.img_dir])
        maparr = down['maparr']
        canstand = down['canstand']
        
        self.unit_sec_list = self.loadUnits(up['unit_list'])
        for unit in self.unit_sec_list:
            unit.setimg(self.imgs[unit.img_dir])
        maparr_sec = up['maparr']
        
        self.width_cnt = down['width_cnt']
        self.height_cnt = down['height_cnt']
        self.unit_width = 32
        self.unit_height = 32
        self.width = self.width_cnt * self.unit_width
        self.height = self.height_cnt * self.unit_height

        self._map =[[None for i in xrange(self.height_cnt)] for j in xrange(self.width_cnt)]
        self._canstand = canstand
        self._map_sec =[[None for i in xrange(self.height_cnt)] for j in xrange(self.width_cnt)]
        for i in xrange(self.width_cnt):
            for j in xrange(self.height_cnt):
                self._map[i][j] = copy.copy(self.unit_list[maparr[i][j]])
                self._map[i][j].mapx = i
                self._map[i][j].mapy = j
                
                if maparr_sec[i][j] is None:
                    self._map_sec[i][j] = None
                else:
                    self._map_sec[i][j] = copy.copy(self.unit_sec_list[maparr_sec[i][j]])
                    self._map_sec[i][j].mapx = i
                    self._map_sec[i][j].mapy = j
                
                

        #for unit in self.unit_list:
        #    self._map[unit.mapx][unit.mapy] = copy.copy(unit)

    def loadImgs(self, r_dir_list):
        imgs = {}
        for dir in r_dir_list:
            img = pygame.image.load(dir).convert_alpha()
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

    def display(self, screen, delta_x = 0, delta_y = 0):
        for arr in self._map:
            for unit in arr:
                unit.display(screen, delta_x, delta_y)
        for arr in self._map_sec:
            for unit in arr:
                if unit is not None:
                    unit.display(screen, delta_x, delta_y)
    def ok(self, x, y, posindex):
        v = [(0, 0), (0, -1), (-1, 0), (-1, -1)]
        x = int(x)
        y = int(y)
        indx = x/self.unit_width + (v[posindex][0] if x % self.unit_width == 0 else 0)
        indy = y/self.unit_height + (v[posindex][1] if y % self.unit_height == 0 else 0)

        if indx >= self.width_cnt:
            return True
        if indy >= self.height_cnt:
            return True
        return 0 == self._canstand[indx][indy]

    def feql(self, a, b):
        return abs(a-b) < 1e-8
    def isallow(self, sx, sy, x, y):
        eps = 3
        x0, y0 = x+eps, y+eps
        x1, y1 = x+self.unit_width-eps, y+eps
        x2, y2 = x+eps, self.unit_height+y-eps
        x3, y3 = x+self.unit_width-eps, self.unit_height+y-eps
        
        def printxy(x0, x1, x2, x3, y0, y1, y2, y3):
            print "x0 y0 : %s %s" % (x0, y0)
            print "x1 y1 : %s %s" % (x1, y1)
            print "x2 y2 : %s %s" % (x2, y2)
            print "x3 y3 : %s %s" % (x3, y3)
            
        if self.feql(sx, x):
            if sy < y: #down
                print "1 : %s %s" % (self.ok(x2, y2, 2), self.ok(x3, y3, 3))
                printxy(x0, x1, x2, x3, y0, y1, y2, y3)
                return self.ok(x2, y2, 2) and self.ok(x3, y3, 3)
               
            elif sy > y: #up
                print "2 : %s %s" % (self.ok(x0, y0, 0), self.ok(x1, y1, 1))
                printxy(x0, x1, x2, x3, y0, y1, y2, y3)
                return self.ok(x0, y0, 0) and self.ok(x1, y1, 1)
               
        if self.feql(sy, y):
            if sx < x: #right
                print "3 : %s %s" % (self.ok(x1, y1, 1), self.ok(x3, y3, 3))
                printxy(x0, x1, x2, x3, y0, y1, y2, y3)
                return self.ok(x1, y1, 1) and self.ok(x3, y3, 3)
            elif sx > x: #left
                print "4 : %s %s" % (self.ok(x0, y0, 0), self.ok(x2, y2, 2))
                printxy(x0, x1, x2, x3, y0, y1, y2, y3)
                return self.ok(x0, y0, 0) and self.ok(x2, y2, 2)
        return True
        
        #return self.ok(x0, y0) and self.ok(x1, y1) and self.ok(x2, y2) and self.ok(x3, y3)
        #print 'x %f y %f indx %d indy %d canstand %d' % (x, y, indx, indy, self._canstand[indx][indy])
        
        

if '__main__' == __name__:
    screen = pygame.display.set_mode((640, 480), 0, 32)
    clock = pygame.time.Clock()
    tmap = tengmap()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        tmap.display(screen)
        pygame.display.update()
        clock.tick(1)#fps 120
