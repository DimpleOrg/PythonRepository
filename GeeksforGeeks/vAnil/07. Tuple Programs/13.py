# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:48:39 2021

@author: ANIL
"""

'''
Python – Convert Nested Tuple to Custom Key Dictionary
'''

test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))

# printing original tuple
print("The original tuple : " + str(test_tuple))

res = [{'key': sub[0], 'value': sub[1], 'id': sub[2]}
							for sub in test_tuple]

# printing result
print("The converted dictionary : " + str(res))
