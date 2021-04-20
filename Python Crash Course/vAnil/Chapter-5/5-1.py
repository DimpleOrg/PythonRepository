# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:41:52 2021

@author: ANIL
"""
car = 'Honda'
print("Is car == 'Honda'? I predict True.")
print(car == 'Honda')

print('\n')

print("Is car == 'audi'? I predict false.")
print(car == 'audi')
print('\n')

if car == 'Honda':
    print('Car is Honda.')
else:
    print('Car is not Honda.')

car = 'Audi'
if car == 'Audi':
    print('Car is Audi.')
elif car == 'Honda':
    print('Car is Honda.')
else:
    print('Car is some other brand.')

print(car == 'Honda')
print(car == 'Audi')
