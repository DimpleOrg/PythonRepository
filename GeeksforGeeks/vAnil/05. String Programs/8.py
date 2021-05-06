# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:24:53 2021

@author: ANIL
"""

'''
Find length of a string in python (4 ways)
Input : 'abc'
Output : 3
'''

str = "geeks"
print(len(str))


count = 0

for c in str:
    count += 1
    
print(count)