# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 18:42:58 2021

@author: dimpl
"""

# =============================================================================
# Given a list of numbers, write a Python program to print all positive numbers in given list.
# 
# Example:
# 
# Input: list1 = [12, -7, 5, 64, -14]
# Output: 12, 5, 64
# =============================================================================

list1 = [12, -7, 5, 64, -14]
print([x for x in list1 if x>0])
