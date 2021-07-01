# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 06:44:47 2021

@author: dimpl
"""

# Join Tuples if similar initial element
# Input : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)]

from collections import defaultdict


test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
res = defaultdict(list)

for each in test_list:
    res[each[0]].append(each[1])

res1 = [(key, *val) for key, val in res.items()]

print(res1)
