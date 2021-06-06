# -*- coding: utf-8 -*-
"""
Created on Sun May 30 13:52:37 2021

@author: ANIL
"""

'''
Extract Unique values dictionary values
'''

test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}

vals = { item for val in test_dict.values() for item in val}

print(vals)


from itertools import chain
res = list(sorted(set(chain(*test_dict.values()))))
print(res)
