# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:42:45 2021

@author: dimpl
"""

# Keys associated with Values in Dictionary

# Input : test_dict = {‘abc’ : [10, 30], ‘bcd’ : [30, 40, 10]}
# Output : {10: [‘abc’, ‘bcd’], 30: [‘abc’, ‘bcd’], 40: [‘bcd’]}

# Input : test_dict = {‘gfg’ : [1, 2, 3], ‘is’ : [1, 4], ‘best’ : [4, 2]}
# Output : {1: [‘is’, ‘gfg’], 2: [‘gfg’, ‘best’], 3: [‘gfg’], 4: [‘is’, ‘best’]}

from collections import defaultdict

test_dict = {"abc": [10, 30], "bcd": [30, 40, 10]}

res = defaultdict(list)
for key, val in test_dict.items():
    for each in val:
        res[each].append(key)

print(res)
