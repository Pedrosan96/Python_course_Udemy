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
    height=input('How tall are you(cm)? ')          #Ask for the weight
    weight=input('How much do you weight(kg)? ')    #Ask for the height
    bmi_val=int(weight)/(int(height)/100)**2        #Calulate the BM index
    print('Your BMI is {}'.format(round(bmi_val,2)))#Show it with 2 decimals
    if (bmi_val < 18.5) :                           #Compare if it is less than
        print('You should better eat more :)')      #the recommended
    elif bmi_val >= 18.5 and bmi_val <= 24:         #Or between the correct ones
        print('Good job! Your BMI is OK')           
    else:                                           #Or an bigger value
        print('You should better do some excercises :(')


def main():
    
    print("Let\'s calculate your Body Mass Index ")
    bmi_app()



if __name__ == "__main__":
    main()

