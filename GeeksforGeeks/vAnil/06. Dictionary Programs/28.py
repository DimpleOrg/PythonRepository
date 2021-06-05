# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:10:35 2021

@author: ANIL
"""

'''
Keys associated with Values in Dictionary
'''
from collections import defaultdict

test_dict = {'gfg' : [1, 2, 3], 'is' : [1, 4], 'best' : [4, 2]}

res = defaultdict(list)
for key, val in test_dict.items():
    for ele in val:
        res[ele].append(key)
        
print(str(dict(res))) 


