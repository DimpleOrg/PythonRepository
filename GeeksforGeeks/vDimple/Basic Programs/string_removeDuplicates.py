# -*- coding: utf-8 -*-
"""
Created on Fri May  7 07:04:47 2021

@author: dimpl
"""

# Remove all duplicates from a given string in Python
string = "geeksforgeeks"
res = ""
res_set = set({})
for i in string:
    if i not in res_set:
        res_set.add(i)
        res += i
print(res)


# Method 2:
from collections import OrderedDict

# removeDupWithoutOrder
res1 = "".join(set(string))
print(res1)

# removeDupWithOrder
res2 = "".join(OrderedDict.fromkeys(string))
print(res2)
