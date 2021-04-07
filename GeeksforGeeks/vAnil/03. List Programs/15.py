# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:51:17 2021

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

s = 4
e = 15

for val in range(s,e+1):
    if val%2 == 0:
        print(val)