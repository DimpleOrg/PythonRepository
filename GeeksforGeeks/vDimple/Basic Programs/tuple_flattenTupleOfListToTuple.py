# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 22:06:47 2021

@author: dimpl
"""

# Flatten tuple of List to tuple
# Input : test_tuple = ([5], [6,7], [3], [8])
# Output : (5, 6, 3, 8)

test_tuple = ([5], [6, 7], [3], [8])
res = tuple(sum(test_tuple, []))
print(res)


# Method #2 : Using tuple() + chain.from_iterable()
from itertools import chain

test_tuple = ([5], [6, 7], [3], [8])
res1 = tuple(chain.from_iterable(test_tuple))
print(res1)
