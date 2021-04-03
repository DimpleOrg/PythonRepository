# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:30:05 2021

@author: ANIL
"""
'''
Given an array of integers, find the sum of its elements.

Examples :

Input : arr[] = {1, 2, 3}
Output : 6
1 + 2 + 3 = 6

Input : arr[] = {15, 12, 13, 10}
Output : 50
'''

arr = [15, 12, 13, 10]
sum = 0

for val in arr:
    sum += val
    
print(sum)