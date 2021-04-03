# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:36:20 2021

@author: ANIL
"""

'''
Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
1) Store d elements in a temp array
   temp[] = [1, 2]
2) Shift rest of the arr[]
   arr[] = [3, 4, 5, 6, 7, 6, 7]
3) Store back the d elements
   arr[] = [3, 4, 5, 6, 7, 1, 2]
'''

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n =7

arr = arr[d+1:n] + arr[:d]

print(arr)

