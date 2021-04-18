# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 08:23:14 2021

@author: dimpl
"""

# Given a list of integers, the task is to find N largest elements assuming 
# size of list is greater than or equal o N.


list1=[3,54,34,65,2]
n=3
list1.sort()
print(list1[n-1:])
print(list1[-n:])