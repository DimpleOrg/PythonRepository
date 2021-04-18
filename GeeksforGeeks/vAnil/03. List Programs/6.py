# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:05:18 2021

@author: ANIL
"""

'''
Python provides us with various ways of reversing a list. We will go through few of the many techniques on how a list in python can be reversed.
Examples:

Input : list = [10, 11, 12, 13, 14, 15]
Output : [15, 14, 13, 12, 11, 10]

Input : list = [4, 5, 6, 7, 8, 9]
Output : [9, 8, 7, 6, 5, 4]
'''

list1 = [10, 11, 12, 13, 14, 15]
print(list1)
list1.reverse()
print(list1)


list1 = [10, 11, 12, 13, 14, 15]
print(list1)
rlist1 = [ val for val in reversed(list1)]
print(rlist1)

list1 = [10, 11, 12, 13, 14, 15]
print(list1)
rlist1 =list1[::-1]
print(rlist1)



