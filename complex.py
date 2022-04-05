#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo para números complejos
"""
import math


class Complex:
    'This class simulates complex numbers'
    def __init__(self, real=0, imag=0):
        self.SetReal(real)
        self.SetImag(imag)

    def GetReal(self):
        return self.__real
    
    def GetImag(self):
        return self.__imag
    
    def GetModulus(self):
        return math.sqrt(self.GetReal()*self.GetReal()+
                self.GetImag()*self.GetImag())
    
    def GetPhi(self):
        return math.atan2(self.GetImag(), self.GetReal())
    
    def SetReal(self, val):
        if type(val) not in (int, float):
            raise Exception('Real part must be a number')
        self.__real=val
    
    def SetImag(self, val):
        if type(val) not in (int, float):
            raise Exception('Imaginary part must be a number')
        self.__imag = val


def main():

    try:

        c = Complex(2, 4)
        print(c.GetReal(),'+',c.GetImag(),'j')
        print('It\'s modulus and angle are:')
        print(c.GetModulus(), c.GetPhi())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

