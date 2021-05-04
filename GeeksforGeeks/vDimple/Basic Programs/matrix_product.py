# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 07:16:41 2021

@author: dimpl
"""

# Python | Matrix Product: Product of all elements in matrix.
A = [[1, 4, 5], [7, 3, 5], [4, 3, 2], [46, 7, 3]]

# Method 1 : Brute Force
prod1 = 1
for i in range(len(A)):
    for j in range(len(A[0])):
        prod1 *= A[i][j]
print(prod1)

# For normal Lists/Matrix
# Method #2 : Using list comprehension + loop
import numpy

test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
result = numpy.prod([each for sub_list in test_list for each in sub_list])
print(result)

# For normal Lists/Matrix
# Method #3 : Using chain() + loop
# =============================================================================
# It is a function that takes a series of iterables and returns one iterable. It
# groups all the iterables together and produces a single iterable as output. Its
#  output cannot be used directly and thus explicitly converted into iterables.
# =============================================================================
from itertools import chain


def prod(l):
    res = 1
    for each in l:
        res *= each
    return res


test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
result1 = prod(list(chain(*test_list)))
print(result1)


# Method 4: List Comprehension
import math

A = [[1, 4, 5], [7, 3, 5], [4, 3, 2], [46, 7, 3]]
print(math.prod([math.prod(each) for each in zip(*A)]))
# print(result2)
