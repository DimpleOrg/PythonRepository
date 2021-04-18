# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:35:40 2021

@author: ANIL
"""

'''
Given a list of numbers, the task is to write a Python program to find the second largest number in given list.
Examples: 

Input: list1 = [10, 20, 4]
Output: 10

Input: list2 = [70, 11, 20, 4, 100]
Output: 70
'''

list2 = [70, 11, 20, 4, 100,111]
max1 = list2[0]
max2 = list2[0]


for val in list2:
    if max1 < val:
        max2 = max1
        max1 = val
                
print(max2)


#method2
list2 = [70, 11, 20, 4, 100,111]
list2.remove(max(list2))
print(max(list2))


