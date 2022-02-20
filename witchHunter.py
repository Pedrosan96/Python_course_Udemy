#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Witch Hunter game implementing classes and inheritance
"""
import random,time

class Witch:
    def __init__(self, name, level):
        self.name=name
        self.level=level

    def __repr__(self):
        print('{} (lv{})'.format(self.name, self.level))

    def witchcraft_attack(self):
        return random.randint(1,10)*self.level

class FireWitch(Witch):
    def __init__(self, name, level, fire_staff):
        super().__init__(name, level)
        self.fire_staff=fire_staff

    def witchcraft_attack(self):
        base_attack=super().witchcraft_attack()
        if self.fire_staff:
            print('Witchcraft is filling with fire!!')
            return base_attack * 2
        else:
            return base_attack

class EvilWitch(Witch):
    def __init__(self, name, level, black_staff_level):
        super().__init__(name, level)
        self.black_staff_level = black_staff_level

    def witchcraft_attack(self):
        base_attack=super().witchcraft_attack()
        print(f'Witchcraft with black staff level{self.black_staff_level}!!')
        return base_attack*2*self.black_staff_level
        

class Hunter:
    def __init__(self, name, level):
        self.name=name
        self.level=level

    def __repr__(self):
        return ('{} lv{}'.format(self.name, self.level))

    def attack(self, witch, critical_strike):
        base_damage = random.randint(1, 10) * self.level
        hunter_damage=base_damage*2 if critical_strike else base_damage
        witch_damage=witch.witchcraft_attack()
        critical_strike_msg = '(critical strike!)'if critical_strike else ''
        print('Hunter attacked {}'.format(hunter_damage))
        print('Witch attacked {}'.format(witch_damage))
        if hunter_damage > witch_damage:
            print('You defeted the witch {}!'.format(witch.name))
            return True
        else:
            print('Run away {}!'.format(self.name))
            return False

def start_game():
    hunter=Hunter('Leumas', 3)

    while True:
        witches=[Witch('Scarlett', random.randint(1,5)),
                FireWitch('FireSabrina', random.randint(6,20), random.choice([True,False])),
                EvilWitch('EvilCarlotta', random.randint(21,30), random.randint(1,3))]
        witch=random.choice(witches)
        print('\n{} has appeared!!\n'.format(witch.name))
        cmd=input('Do you [a]ttack or [s]top tracing, [q]uit?')
        if cmd=='a':
            if hunter.attack(witch, random.choice([True, False])):
                hunter.level +=1
                print(f'Level up! {hunter.level} level now')
            else:
                print('Hunter is taking time to recover')
                time.sleep(1)
        elif cmd=='q':
            break
        else:
            print('Hunter stopped tracing')



if __name__ == "__main__":
    start_game()

