# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:55:57 2021

@author: ANIL
"""

'''
Given a list, write a Python program to swap first and last element of the list.

Examples:

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
'''

arr = [12, 35, 9, 56, 24]

arr[0], arr[-1] = arr[-1], arr[0]

print(arr)