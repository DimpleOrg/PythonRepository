# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:31:39 2021

@author: ANIL
"""

'''
Given a list of numbers, the task is to write a Python program to find the smallest number in given list.
Examples: 

Input : list1 = [10, 20, 4]
Output : 4

Input : list2 = [20, 10, 20, 1, 100]
Output : 1
'''

list1 = [10, 20, 4]

print(min(list1))

minVal = list1[0]

for val in list1:
    if minVal > val:
        minVal = val
        
print(minVal)