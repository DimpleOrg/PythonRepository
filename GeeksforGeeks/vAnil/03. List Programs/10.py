# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:33:15 2021

@author: ANIL
"""

'''
Given a list of numbers, the task is to write a Python program to find the largest number in given list.

Examples:

Input : list1 = [10, 20, 4]
Output : 20

Input : list2 = [20, 10, 20, 4, 100]
Output : 100
'''

list1 = [10, 20, 4]

print(max(list1))

maxVal = list1[0]

for val in list1:
    if maxVal < val:
        maxVal = val
        
print(maxVal)