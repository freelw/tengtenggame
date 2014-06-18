#!/usr/bin/env python
#coding=utf-8

import pygame
from pygame.locals import *
pygame.init()
import json
import sys

def saveinfo(info, width, height):
    ulist = []
    maparr = [[0 for j in xrange(height)] for i in xrange(width)]
    
    def getind(item, ulist):
        cnt = 0
        for u in ulist:
            if u['indx'] == item['indx'] and u['indy'] == item['indy']:
                return cnt
            cnt += 1
        tmp = {"img_dir":"./pic/map.png", "indx":item['indx'], "indy":item['indy']}
        ulist.append(tmp)
        return cnt

    for i in xrange(width):
        for j in xrange(height):
            if info[i][j] is not None:
                ind = getind(info[i][j], ulist)
                maparr[i][j] = ind
        
    res = {"unit_list":ulist,
    "width_cnt":width,
    "height_cnt":height,
    "maparr":maparr}
    
    res = json.dumps(res)
    
    f = open('./buildmapinfo', 'w')
    f.write(res)
    f.close()
            
if '__main__' == __name__:
    if len(sys.argv) < 3:
        print 'argv error'
        exit()
    
    if '-f' == sys.argv[1]:
        fname = sys.argv[2]
        f = open(fname)
        content = ''
        for line in f:
            content += line
        f.close()
        tmp = json.loads(content)
        mapw = tmp['width_cnt']
        maph = tmp['height_cnt']
        ulist = tmp['unit_list']
        arr = tmp['maparr']
        mapinfo = [[None for j in xrange(maph)] for i in xrange(mapw)]
        for i in xrange(mapw):
            for j in xrange(maph):
                mapinfo[i][j] = {'indx':ulist[arr[i][j]]['indx'], 'indy':ulist[arr[i][j]]['indy']}
    else:
        mapw = int(sys.argv[1])
        maph = int(sys.argv[2])
        mapinfo = [[None for j in xrange(maph)] for i in xrange(mapw)]
    sw = 1500
    sh = 480
    screen = pygame.display.set_mode((sw, sh), 0, 32)
    clock = pygame.time.Clock()
    black = pygame.Color(0, 0, 0, 0)
    green = pygame.Color(0, 255, 0, 0)
    blue = pygame.Color(0, 0, 255, 0)
    delta_x = 0
    delta_y = 0
    width = 32
    height = 32
    img = pygame.image.load('./pic/map.png').convert()
    indx = 0
    indy = 0
    vector = [{'x':0, 'y':1}, {'x':-1, 'y':0}, {'x':1, 'y':0}, {'x':0, 'y':-1}]
    kposy = {K_DOWN:0, K_LEFT:1, K_RIGHT:2, K_UP:3}    
    bleft = True
    indmx = 0
    indmy = 0
    delta_mx = 0
    delta_my = 0
    
    basex = 9 * width
    basey = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if K_TAB == event.key:
                    bleft = not bleft
                if bleft:
                    if K_RETURN == event.key:
                        saveinfo(mapinfo, mapw, maph)
                    for key in kposy:
                        if key == event.key:
                            indx += vector[kposy[key]]['x']
                            indy += vector[kposy[key]]['y']
                            if indx < 0:
                                indx = 0
                            if indy < 0:
                                indy = 0
                            if indx >= 8:
                                indx = 7
                            if indy >= 112:
                                indy = 111
                            while delta_y * height + sh < indy * height + height:
                                delta_y += 1
                            while delta_y * height > indy * height:
                                delta_y -= 1
                else: # not bleft
                    if K_RETURN == event.key:
                        mapinfo[indmx][indmy] = {'indx':indx, 'indy':indy}
                    for key in kposy:
                        if key == event.key:
                            indmx += vector[kposy[key]]['x']
                            indmy += vector[kposy[key]]['y']
                            if indmx < 0:
                                indmx = 0
                            if indmy < 0:
                                indmy = 0
                            if indmx >= mapw:
                                indmx = mapw-1
                            if indmy >= maph:
                                indmy = maph-1
                            while delta_my * height + sh < indmy * height + height:
                                delta_my += 1
                            while delta_my * height > indmy * height:
                                delta_my -= 1
                            while delta_mx * width + sw - basex < indmx * width + width:
                                delta_mx += 1
                            while delta_mx * width > indmx * width:
                                delta_mx -= 1
        pygame.draw.rect(screen, black, (0, 0, sw, sh))
        
        for j in xrange(maph):
            for i in xrange(mapw):
                if mapinfo[i][j] is not None:
                    screen.blit(img, (basex+i*width-delta_mx*width, basey+j*width-delta_my*height), (mapinfo[i][j]['indx']*width, mapinfo[i][j]['indy']*height, width, height))
        pygame.draw.rect(screen, blue if bleft else green, (basex + (indmx - delta_mx)*width, basey + (indmy - delta_my) * height, width, height), 2)
        screen.blit(img, (0, 0), (delta_x * width, delta_y * height, img.get_width(), img.get_height()))
        pygame.draw.rect(screen, blue if not bleft else green, ((indx - delta_x)*width, (indy - delta_y) * height, width, height), 2)
        pygame.display.update()
        clock.tick(30)#fps 120