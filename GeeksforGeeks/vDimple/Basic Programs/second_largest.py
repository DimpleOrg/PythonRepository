# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 08:12:40 2021

@author: dimpl
"""

# =============================================================================
# Given a list of numbers, the task is to write a Python program to find the second largest number in given list.
# Examples: 
# 
# Input: list1 = [10, 20, 4]
# Output: 10
# =============================================================================

list1 = [10, 20, 4]
list1.remove(max(list1))
print(max(list1))

#----------------------------------Mehtod 2---------------------

list1=[10,20,4]
list1.sort()
print(list1[-2])