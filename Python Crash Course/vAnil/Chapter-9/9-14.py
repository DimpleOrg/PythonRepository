# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:04:52 2021

@author: ANIL
"""

from random import choice

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

print('Any ticket matching these four numbers or letters wins a prize:')
print(choice(data))
print(choice(data))
print(choice(data))
print(choice(data))
