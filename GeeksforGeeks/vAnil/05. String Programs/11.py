# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:45:19 2021

@author: ANIL
"""

'''
Given a pair of non empty strings. Count the number of matching characters in those strings 
(consider the single count for the character which have duplicates in the strings).

Examples:

Input : str1 = 'abcdef'
        str2 = 'defghia'
Output : 4 
'''
str1 = 'abcdef'
str2 = 'defghia'

set1 = set(str1) & set(str2)

print(f'Number of matching chars: {len(set1)}')