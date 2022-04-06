#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo para la busqueda de patrones usando re(Regular Expressions)
"""
import re

def all_matches(text, pattern):
    print(pattern)
    regobj = re.compile(pattern)
    for m in regobj.finditer(text):
        print(str(m.start()) + '-' + str(m.end()) + ': ' +
                text[m.start():m.end()])

all_matches('xyyxxxxxyyyyxxxxyy', 'xy*')
all_matches('xyyxxxxxyyyyxxxxyy', 'xy+')
all_matches('xyyxxxxxyyyyxxxxyy', 'xy?')
all_matches('xyyxxxxxyyyyxxxxyy', 'xy{3,4}')    #entre 3 y 4
all_matches('xyyxxxxxyyyyxxxxyy', 'xy{2,}') #Para dos o mas


all_matches('xx..  ..yyyxxx.. ', '[^. ]+') #Que no contenga espacios ni puntos

all_matches('A94B3c42  xyz08', '[A-Za-z][0-9]') #Para combinaciones de mueros y
                                             #letras

all_matches('Silk Road', 'S.+k') #Que empiecen con S y terminen con k


all_matches('This is the 1-st example', r'\d+') #solo numeros
all_matches('This is the 1-st example', r'\D+') #Todo menos numeros
all_matches('This is the 1-st example', r'\s+') #solo espacios
all_matches('This is the 1-st example', r'\S+') #Todo menos espacios


