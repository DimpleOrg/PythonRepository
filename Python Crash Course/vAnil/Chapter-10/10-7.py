# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:19:57 2021

@author: ANIL
"""

while True:
    print('\n\nEnter q to quit.')
    num1 = input('Input first number: ')
    if num1 == 'q':
        break
    num2 = input('Input second number: ')
    if num2 == 'q':
        break
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print('\nError: Entered number is not a valid number.'
              '\nPlease enter the valid numbers.')
    else:
        print(f'\n\nAddition\n {num1} + {num2} = {num1+num2}')
