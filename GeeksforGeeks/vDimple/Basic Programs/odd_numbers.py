# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 08:29:20 2021

@author: dimpl
"""

# =============================================================================
# Given a list of numbers, write a Python program to print all odd numbers in given list.
# 
# Example:
# 
# Input: list1 = [2, 7, 5, 64, 14]
# Output: [7, 5]
# =============================================================================

list1 = [2, 7, 5, 64, 14]
odd_num=[each for each in list1 if each%2!=0]
print(odd_num)