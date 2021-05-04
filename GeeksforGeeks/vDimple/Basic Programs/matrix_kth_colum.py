# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:38:52 2021

@author: dimpl
"""

# Python | Get Kth Column of Matrix
# The original list is : [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
# K = 2
# The Kth column of matrix is : [6, 10, 5]

# METHOD 1:
test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
k = 2
res = [sub_list[k] for sub_list in test_list]
print(res)

# METHOD 2:
res_list = list(zip(*test_list))[k]
print(res_list)
