# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:31:03 2021

@author: ANIL
"""

'''
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

Examples:

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
'''

arr = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

pos1 -=1
pos2 -=1

if pos1 < len(arr) and pos2 < len(arr):
    arr[pos1], arr[pos2] = arr[pos2],arr[pos1]
    
print(arr)