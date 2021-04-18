# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:47:12 2021

@author: ANIL
"""

'''
Given a list of numbers, write a Python program to print all odd numbers in given list.

Example:

Input: list1 = [2, 7, 5, 64, 14]
Output: [7, 5]

Input: list2 = [12, 14, 95, 3, 73]
Output: [95, 3, 73]
'''

list2 = [12, 14, 95, 3, 73]

for val in list2:
    if val%2 != 0:
        print(val)
        
        
odd2 = [num for num in list2 if num % 2 == 1]
print(odd2)