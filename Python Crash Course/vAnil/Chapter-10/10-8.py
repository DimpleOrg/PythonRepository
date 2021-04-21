# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:29:01 2021

@author: ANIL
"""
try:
    with open('cat.txt') as f:
        cats = f.read()
except:
    print('\nError: cat.txt file is not present in current directory.')
else:
    print('\nCats:')
    print(cats)

try:
    with open('dog.txt') as f:
        dogs = f.read()
except:
    print('\nError: dog.txt file is not present in current directory.')
else:
    print('\nDogs:')
    print(dogs)
