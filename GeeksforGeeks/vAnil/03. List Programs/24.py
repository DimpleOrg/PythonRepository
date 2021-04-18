# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:45:56 2021

@author: ANIL
"""

'''
Count occurrences of an element in a list

Given a list in Python and a number x, count number of occurrences of x in the given list.

Examples:

Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
         x = 10
Output : 3 
10 appears three times in given list.

Input : lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
        x = 16
Output : 0
'''


lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10

print(f'Count of {x} is {lst.count(x)}')