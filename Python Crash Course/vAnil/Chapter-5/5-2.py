# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:48:34 2021

@author: ANIL
"""

str = 'hello'
if str == 'hello':
    print('str == \'hello\'? is True.')
elif str == 'hello':
    print('str == \'hello\'? is False.')

if str.upper() == 'HELLO':
    print('str == \'HELLO\'? is True.')

x = 'Ten'
if x.lower() == 'ten':
    print('x == \'ten\' is True.')
elif x.upper() == 'TEN':
    print('x == \'TEN\' is True')
else:
    print('x is not upper or lower')

y = 10
if y == 10:
    print('Value of y is 10.')
elif y > 10:
    print('Value of y is greater than 10.')
elif y < 10:
    print('Value of y is less than 10.')

z = 50
if z >= 40:
    print('Value of z is greater than equal to 40.')
else:
    print('Value of z is less than 40.')

if z <= 40:
    print('Value of z is less than equal to 40.')
else:
    print('Value of z is greater than 40.')

if x == 'Ten' and y == 10:
    print('x==Ten and y==10')
elif x == 'Ten' or y == 10:
    print('x==Ten or y==10')
else:
    print('Unexpected output')


cars = ['Honda', 'Audi', 'Maruti']
if 'Honda' in cars:
    print('Honda car is present.')
if 'Ford' in cars:
    print('Ford car is not present.')
