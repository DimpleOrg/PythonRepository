# -*- coding: utf-8 -*-
"""
Created on Fri May 14 07:42:57 2021

@author: dimpl
"""

# Permutation of a given string using inbuilt function
from itertools import permutations

str = "ABCC"
permutations_list = permutations(str)

# print all permutations
for perm in list(permutations_list):
    print("".join(perm))


# Permutations of a given string with repeating characters
# The idea is to use dictionary to avoid printing duplicates.
print("************Method 2**********")
from itertools import permutations

str = "ABCC"
p = permutations(str)

d = []
for i in list(p):
    if i not in d:
        d.append(i)
        print("".join(i))
