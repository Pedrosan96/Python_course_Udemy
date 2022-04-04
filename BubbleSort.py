#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""

Algoritmo de ordemaniento burbuja

"""
import random

array = []


def bSort(tam):

    print('vector ordenado:')
    print('[')
    for i in range(tam):
        for pos in range(tam-1-i):
            if array[pos] < array[pos+1]:
                aux = array[pos]
                array[pos]=array[pos+1]
                array[pos+1]=aux
        print(array[tam-1-i])
    print(']')

def main():

    print("Hola, esta es una app para ordenar un vector por el método burbuja")
    tamanio = int(input('Ingresa el tamaño del vector a ordenar: '))
    for pos in range(tamanio):
        numero = float(input('Valor {}: '.format(pos)))
        array.append(numero)

    bSort(tamanio)
    


if __name__ == "__main__":
    main()

