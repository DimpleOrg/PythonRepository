# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:50:34 2021

@author: ANIL
"""

'''
Given starting and end points, write a Python program to print all even numbers in that given range.

Example:

Input: start = 4, end = 15
Output: 4, 6, 8, 10, 12, 14

Input: start = 8, end = 11
Output: 8, 10
'''

list2 = [12, 14, 95, 3, 73]

for val in list2:
    if val%2 == 0:
        print(val)
        
        
odd2 = [num for num in list2 if num % 2 == 0]
print(odd2)