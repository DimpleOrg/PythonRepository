# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 17:15:08 2021

@author: dimpl
"""
# =============================================================================
# 
# Given starting and end points, write a Python program to print all even numbers in that given range.
# 
# Example:
# 
# Input: start = 4, end = 15
# Output: 4, 6, 8, 10, 12, 14
# =============================================================================

start = 4
end = 15
even_nos=[x for x in range(start,end+1) if x%2==0]
print(*even_nos)