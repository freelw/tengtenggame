
#!/usr/bin/env python
#coding=utf-8

from tengfight import *

class simplefight(tengfight):
    def __init__(self, surface):
        tengfight.__init__(self, surface)
        hero1 = soldier('./pic/153.png', 'lw', 90, 200, 2, 1, 1, 0, 64, 32, 32)
        monster1 = soldier('./pic/12.png', 'monster', 300, 80, 2, 1, 0)
        self.hero = hero1
        self.monster = monster1

    def get_hero(self):
        return self.hero
    def get_monster(self):
        return self.monster
