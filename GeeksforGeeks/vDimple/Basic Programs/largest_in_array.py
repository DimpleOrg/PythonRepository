# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 22:58:06 2021

@author: dimpl
"""

# Python Program to find largest element in an array

arr = [10, 20, 4]
max = arr[0]
for i in arr:
    if max < i:
        max = i
print(max)
