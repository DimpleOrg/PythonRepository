# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 00:13:29 2021

@author: dimpl
"""

# =============================================================================
# Given a list, write a Python program to swap first and last element of the list.
#
# Examples:
#
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]
#
# =============================================================================

my_list = [1, 2, 3, 4]
temp = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = temp
print(my_list)
