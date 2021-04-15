# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:49:37 2021

@author: ANIL
"""

'''
Given start and end of a range, write a Python program to print all positive numbers in given range.

Example:

Input: start = -4, end = 5
Output: 0, 1, 2, 3, 4, 5 

Input: start = -3, end = 4
Output: 0, 1, 2, 3, 4
'''

start = -4
end = 5

for val in range(start,end+1):
    if val >=0:
        print(val)