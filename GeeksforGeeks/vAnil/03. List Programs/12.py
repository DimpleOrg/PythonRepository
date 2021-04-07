# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:41:38 2021

@author: ANIL
"""

'''
Given a list of integers, the task is to find N largest elements assuming size of list is greater than or equal o N.

Examples :

Input : [4, 5, 1, 2, 9] 
        N = 2
Output :  [9, 5]

Input : [81, 52, 45, 10, 3, 2, 96] 
        N = 3
Output : [81, 96, 52]
'''

lst = [81, 52, 45, 10, 3, 2, 96] 
N = 3

lst.sort()

print(lst[len(lst)-1:len(lst)-N-1:-1])

#or
print(lst[-N:])