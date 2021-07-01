# -*- coding: utf-8 -*-
"""
Created on Fri May 14 07:14:15 2021

@author: dimpl
"""

# Replace duplicate Occurrence in String

# Method1: enumerate()
# =============================================================================
# values = ["a", "b", "c"]
# for count, value in enumerate(values):
# ...     print(count, value)
# ...
# 0 a
# 1 b
# 2 c
#
# for count, value in enumerate(values, start=1):
# ...     print(count, value)
# ...
# 1 a
# 2 b
# 3 c
# =============================================================================
test_str = "Gfg is best . Gfg also has Classes now. \
                Classes help understand better . "
# initializing replace mapping
repl_dict = {"Gfg": "It", "Classes": "They"}
test_list = test_str.split()
res = set()
for index, ele in enumerate(test_list):
    if ele in repl_dict:
        if ele in res:
            test_list[index] = repl_dict[ele]
        else:
            res.add(ele)
print(" ".join(test_list))


# Method 2: index()
# The index() method returns the position at the first occurrence of the specified value.

test_str = "Gfg is best . Gfg also has Classes now. Classes help understand better . "
repl_dict = {"Gfg": "It", "Classes": "They"}
test_list = test_str.split(" ")

res = " ".join(
    [
        repl_dict.get(ele)
        if ele in repl_dict.keys() and test_list.index(ele) != idx
        else ele
        for idx, ele in enumerate(test_list)
    ]
)
print(res)
