#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Witch Hunter game implementing classes and inheritance
"""
import random

class Witch:
    def __init__(self, name, level):
        self.name=name
        self.level=level

    def __repr__(self):
        print('{} (lv{})'.format(self.name, self.level))

    def witchcraft_attack(self):
        return random.randint(1,10)*self.level
    
class Hunter:
    def __init__(self, name, level):
        self.name=name
        self.level=level

    def __repr__(self):
        return ('{} lv{}'.format(self.name, self.level))

    def attack(self, witch):
        hunter_damage = random.randint(1, 10) * self.level
        witch_damage=witch.witchcraft_attack()
        print('Hunter attacked {}'.format(hunter_damage))
        print('Witch attacked {}'.format(witch_damage))
        if hunter_damage > witch_damage:
            print('You defeted the witch {}!'.format(witch.name))
            return True
        else:
            print('Run away {}!'.format(self.name))
            return False



def main():
    witch = Witch('Scarlett', 5)
    hunter = Hunter('Leumas', 3)

    hunter.attack(witch)


if __name__ == "__main__":
    main()

