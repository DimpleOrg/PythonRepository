# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 08:03:08 2021

@author: dimpl
"""

# Extract digits from Tuple list
# Input : test_list = [(15, 3), (3, 9)]
# Output : [9, 5, 3, 1]

test_list = [(15, 3), (3, 9)]
res = "".join(str(val) for each in test_list for val in each)

res1 = set(res)
print(res1)


# Method 2:Using map() + chain.from_iterable() + set() + loop
from itertools import chain

# initializing list
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]

temp = map(lambda ele: str(ele), chain.from_iterable(test_list))
res = set()
for each in temp:
    for ele in each:
        res.add(ele)

print(res)
