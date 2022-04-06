#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo para usarlo en Debbuging
"""

def Test(a,b):
    suma =0
    for i in range(b):
        suma += i*a   ##de esta menera se puede entrar desde terminal con 
                      ##el comando: python3 -m pdb testDebbug.py
