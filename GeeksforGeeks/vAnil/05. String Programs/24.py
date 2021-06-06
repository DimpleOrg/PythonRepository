# -*- coding: utf-8 -*-
"""
Created on Sun May 16 12:22:39 2021

@author: ANIL
"""

'''
Python | Permutation of a given string using inbuilt function
'''

from itertools import permutations

str = 'ANIL'

permList =["".join(item) for item in permutations(str)]

print(*permList)