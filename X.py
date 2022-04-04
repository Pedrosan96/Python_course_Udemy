#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de una exception personalizada 
"""
var = -1.0

def IntegerException(a):
    """
    El objetivo es verificar el tipo de dato que entra
    """
    if type(a) != type(1):
        raise ValueError("This is not an integer")

def PositiveAssertion(a):
    assert a > 0, "This is not a positive number"

try:
    IntegerException(var)
except ValueError as e:
    print(e)
    
try:
    PositiveAssertion(var)
except AssertionError as e:
    print(e)



