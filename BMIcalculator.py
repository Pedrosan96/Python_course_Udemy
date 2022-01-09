#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Example for a BMI(Body mass index) calculator
"""
def bmi_app():
    height=input('How tall are you(cm)? ')
    weight=input('How much do you weight(kg)? ')
    bmi_val=int(weight)/(int(height)/100)**2
    print('Your BMI is {}'.format(round(bmi_val,2)))
    if (bmi_val < 18.5) :
        print('You should better eat more :)')
    elif bmi_val >= 18.5 and bmi_val <= 24:
        print('Good job! Your BMI is OK')
    else:
        print('You should better do some excercises :(')


def main():
    
    print("Hola Mundo")
    bmi_app()



if __name__ == "__main__":
    main()

