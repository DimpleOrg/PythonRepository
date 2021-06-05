# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:48:04 2021

@author: ANIL
"""

'''
Python – Flatten tuple of List to tuple
'''

# initializing tuple
test_tuple = ([5, 6], [6, 7, 8, 9], [3])

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Flatten tuple of List to tuple
# Using sum() + tuple()
res = tuple(sum(test_tuple, []))

# printing result
print("The flattened tuple : " + str(res))
