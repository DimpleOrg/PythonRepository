# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 18:46:38 2021

@author: dimpl
"""

# =============================================================================
# Given start and end of a range, write a Python program to print all positive numbers in given range.
# 
# Example:
# 
# Input: start = -4, end = 5
# Output: 0, 1, 2, 3, 4, 5 
# =============================================================================

start = -10
end = 10
if start<0:
    print(*[x for x in range(0,end+1) if x>=0])
else:
    print(*[x for x in range(start,end+1)])


# =============================================================================
# Given start and end of a range, write a Python program to print all negative numbers in given range.
# 
# Example:
# 
# Input: start = -4, end = 5
# Output: 0, 1, 2, 3, 4, 5 
# =============================================================================


start = -3
end = 5
if end>0:
    print(*[x for x in range(start,0)]) # * helps display individual element in list
else:
    print(*[x for x in range(start,end+1)])