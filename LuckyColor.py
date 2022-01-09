#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Code to guess a color using lists
"""
import random

def main():
    
    colors=['red','blue','green','purple','yellow','black']
    #luckyColor=colors[random.randint(0,len(colors))]
    luckyColor=random.choice(colors)
    print('You have 3 chances to get the lucky color')
    for chance in range(3):
        print('There are {} colors'.format(colors))
        userColor=input('Guess your lucky color: ')
        if userColor != luckyColor:
            print('Seems like {} is not your lucky color :('.format(userColor))
            colors.remove(userColor)
        else:
            break

    if userColor == luckyColor:
        print('Great your lucky color is {}!'.format(luckyColor))
    else:
        print('Actually your lucky color is {}'.format(luckyColor))



if __name__ == "__main__":
    main()

