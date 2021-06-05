# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 07:54:43 2021

@author: ANIL
"""

'''
 Maximum and Minimum K elements in Tuple
'''
k=2
test_tup = (5, 20, 3, 7, 6, 8)

test_list = list(test_tup)

test_list = sorted (test_list)

result_tuple = tuple(test_list[:k]+test_list[-k:])

print(result_tuple)