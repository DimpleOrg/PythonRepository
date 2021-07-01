# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 22:43:39 2021

@author: dimpl
"""

# All pair combinations of 2 tuples
# Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

test_tuple1 = (7, 2)
test_tuple2 = (7, 8)

res = []

for val1 in test_tuple1:
    for val2 in test_tuple2:
        res.append((val1, val2))
        res.append((val2, val1))

print(res)


# Method #1 : Using list comprehension
res1 = [(val1, val2) for val1 in test_tuple1 for val2 in test_tuple2]
res1 += [(val2, val1) for val1 in test_tuple1 for val2 in test_tuple2]
print(res1)


# Method #2 : Using chain() + product()
from itertools import chain, product

res2 = list(chain(product(test_tuple1, test_tuple2), product(test_tuple2, test_tuple1)))
print(res2)
