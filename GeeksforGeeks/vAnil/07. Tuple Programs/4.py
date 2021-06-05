# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 08:19:15 2021

@author: ANIL
"""

'''
Python – Adding Tuple to List and vice – versa
'''

test_list = [5, 6, 7]
test_tup = (9, 10)


test_list += test_tup


print(test_list)


test_list = [5, 6, 7]
test_tup = (9, 10)


test_tup += tuple(test_list)

print(test_tup)