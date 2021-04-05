# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:01:37 2021

@author: ANIL
"""

'''
Python Program to Split the array and add the first part to the end
'''

arr = [1, 2, 3, 4, 5, 6, 7]
k = 2


arr = arr[k+1:] + arr[:k]

print(arr)