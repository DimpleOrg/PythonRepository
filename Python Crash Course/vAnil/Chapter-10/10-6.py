# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:14:06 2021

@author: ANIL
"""

num1 = input('Input first number: ')
num2 = input('Input second number: ')
try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print('\nError: Entered number is not a valid number.')
else:
    print(f'\n\nAddition\n {num1} + {num2} = {num1+num2}')
