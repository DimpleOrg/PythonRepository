# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 17:36:15 2021

@author: dimpl
"""

# =============================================================================
# Given starting and end points, write a Python program to print all odd numbers in that given range.
# 
# Example:
# 
# Input: start = 4, end = 15
# Output: 5, 7, 9, 11, 13, 15
# =============================================================================

start = 4
end = 15
odd_nos=[x for x in range(start,end+1) if x%2!=0]
print(*odd_nos)