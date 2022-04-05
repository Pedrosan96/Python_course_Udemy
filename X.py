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


def MyDigitCounter(a):
    '''
    El objetivo es contar el numero de digitos en un número
    '''
    div = a/10
    if div < 1:
        return 1
    elif div < 10:
        return 2
    else:
        return 3


def main():
    #Primer requerimiento: entero positivo
    val1=int(float(input('Dime el primer numero: ')))
    try:
        IntegerException(val1)
    except ValueError as e:
        print(e)

    try:
        PositiveAssertion(val1)
    except AssertionError as e:
        print(e)

    val2=int(float(input('Dime el segundo numero: ')))
    try:
        IntegerException(val1)
    except ValueError as e:
        print(e)
    
    try:
        PositiveAssertion(val1)
    except AssertionError as e:
        print(e)
    
    ##Segundo requerimirnto: Numeros con el mismo numero de digitos
    if MyDigitCounter(val1) == MyDigitCounter(val2):
        return 'La suma es: ',  val1+val2
    else:
        return 'Numero de digitos diferente'


print(main())
