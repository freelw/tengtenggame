
#!/usr/bin/env python
#coding=utf-8

from tengfight import *

class simplefight(tengfight):
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
