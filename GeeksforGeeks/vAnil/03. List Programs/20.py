# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:50:59 2021

@author: ANIL
"""

'''
Given start and end of a range, write a Python program to print all negative numbers in given range.

Example:

Input: start = -4, end = 5
Output: -4, -3, -2, -1

Input: start = -3, end = 4
Output: -3, -2, -1
'''
start = -4
end = 5

for val in range(start,end+1):
    if val <0:
        print(val, end=",")