# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:52:31 2021

@author: ANIL
"""
num = input('Tell me a number: ')
num = int(num)
if num % 10 == 0:
    print(f'{num} is a multiple of 10.')
else:
    print(f'{num} is not a multiple of 10.')
