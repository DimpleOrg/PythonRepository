# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 00:16:08 2021

@author: dimpl
"""

# =============================================================================
# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
#
# Examples:
#
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]
# =============================================================================

my_list = [23, 65, 19, 90]
pos1 = 0
pos2 = 2
if pos1 < len(my_list) and pos2 < len(my_list):
    temp = my_list[pos1]
    my_list[pos1] = my_list[pos2]
    my_list[pos2] = temp
    print(my_list)
