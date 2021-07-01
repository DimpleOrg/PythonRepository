# -*- coding: utf-8 -*-
"""
Created on Sun May 30 11:58:27 2021

@author: dimpl
"""
# Append Dictionary Keys and Values ( In order ) in dictionary

# Input : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3}
# Output : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3]
# Explanation : All the keys before all the values in list.

test_dict = {"Gfg": 1, "is": 2, "Best": 3}
ans = list(test_dict.keys()) + list(test_dict.values())
print(ans)


# Method #2 : Using chain() + keys() + values()
from itertools import chain

test_dict = {"Gfg": 1, "is": 2, "Best": 3}
res = list(chain(test_dict.keys(), test_dict.values()))
print(res)
