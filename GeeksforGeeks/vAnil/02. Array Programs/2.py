# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:34:32 2021

@author: ANIL
"""

'''
Given an array, find the largest element in it.

Input : arr[] = {10, 20, 4}
Output : 20

Input : arr[] = {20, 10, 20, 4, 100}
Output : 100
'''

arr = [20, 10, 20, 4, 100]

maxVal = arr[0]

for val in arr:
    if val > maxVal:
        maxVal = val
        
print(f'Largest element is: {maxVal}')