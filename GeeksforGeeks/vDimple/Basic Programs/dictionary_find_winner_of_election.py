# -*- coding: utf-8 -*-
"""
Created on Sat May 29 08:43:35 2021

@author: dimpl
"""

# Dictionary and counter in Python to find winner of election
from collections import Counter

input = [
    "john",
    "johnny",
    "jackie",
    "johnny",
    "john",
    "jackie",
    "jamie",
    "jamie",
    "john",
    "johnny",
    "jamie",
    "johnny",
    "john",
]

res_dict = Counter(input)
max_votes = sorted(res_dict.values(), reverse=True)[0]
lis = []
for key, val in res_dict.items():
    if val == max_votes:
        lis.append(key)
print(sorted(lis)[0])
