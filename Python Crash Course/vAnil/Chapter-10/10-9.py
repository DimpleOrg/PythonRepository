# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:34:17 2021

@author: ANIL
"""

try:
    with open('cat.txt') as f:
        cats = f.read()
except:
    pass
else:
    print('\nCats:')
    print(cats)

try:
    with open('dog.txt') as f:
        dogs = f.read()
except:
    pass
else:
    print('\nDogs:')
    print(dogs)
