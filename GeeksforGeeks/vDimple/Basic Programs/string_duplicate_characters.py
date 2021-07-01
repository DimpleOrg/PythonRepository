# -*- coding: utf-8 -*-
"""
Created on Mon May 24 12:09:48 2021

@author: dimpl
"""

# Find all duplicate characters in string
# Input : hello
# Output : l

# Input : geeksforgeeeks
# Output : e g k s

str = "geeeeeksforgeeks"
set_str = set()
set_res = set()
for i in str:
    if i in set_str:
        set_res.add(i)
    else:
        set_str.add(i)
print(*set_res)


# **************************** Method 2 ******************
from collections import Counter

str_a = "geeksforgeeks"
res = Counter(str_a)
for key in res.keys():
    if res[key] > 1:
        print(key)
