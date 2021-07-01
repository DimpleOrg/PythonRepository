# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 06:23:34 2021

@author: dimpl
"""

# Python program to create a list of tuples from given list having number and its
# cube in each tuple.
# Input: list = [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]

test_list = [1, 2, 3]
res = [(each, pow(each, 3)) for each in test_list]  # or each**3

print(res)
