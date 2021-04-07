# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:57:19 2021

@author: ANIL
"""

'''
Given starting and end points, write a Python program to print all odd numbers in that given range.

Example:

Input: start = 4, end = 15
Output: 5, 7, 9, 11, 13, 15

Input: start = 3, end = 11
Output: 3, 5, 7, 9, 11
'''

s = 4
e = 15

for val in range(s,e+1):
    if val%2 != 0:
        print(val)