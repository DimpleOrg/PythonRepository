# -*- coding: utf-8 -*-
"""
Created on Mon May  3 04:33:47 2021

@author: ANIL
"""

'''
Python | Get Kth Column of Matrix
'''

test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]

k = 1


kth = [ row[k] for row in test_list]

print(kth)