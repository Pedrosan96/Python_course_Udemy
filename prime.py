#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo para encontrar números primos
"""

def IsPrime(n):
    for x in range(2, n // 2+1):
        if not n % x:
            return False
    return True

def PrimesTo(n):
    for x in range(2, n):
        if IsPrime(x):
            print(x)

PrimesTo(50)

