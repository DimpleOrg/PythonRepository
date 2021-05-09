# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:01:00 2021

@author: ANIL
"""

'''
Python | Check if a given string is binary string or not

Input: str = "01010101010"
Output: Yes

Input: str = "geeks101"
Output: No
'''

string = "a"

binSet = set('01')

rSet = binSet.intersection(string)

if len(set(string)) > 2:
    print('No')
elif len(binSet.union(string)) > 2:   
    print('No')
else:
    print('Yes')

