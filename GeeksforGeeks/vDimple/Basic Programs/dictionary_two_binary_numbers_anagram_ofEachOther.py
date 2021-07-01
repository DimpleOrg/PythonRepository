# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:56:55 2021

@author: dimpl
"""

# Given two numbers you are required to check whether they are anagrams of each other or not in binary representation.

# Examples:

# Input : a = 8 (1000), b = 4(0100)
# Output : Yes
# Binary representations of both
# numbers have same 0s and 1s.

# Input : a = 4(100), b = 5(101)
# Output : No

from collections import Counter

a = 8
b = 16

bin_a = bin(a)[2:]
bin_b = bin(b)[2:]

len_diff = abs(len(bin_a) - len(bin_b))
for i in range(len_diff):
    if a > b:
        bin_b = "0" + bin_b
    if b > a:
        bin_a = "0" + bin_a

dict_a = Counter(bin_a)
dict_b = Counter(bin_b)

if dict_a == dict_b:
    print("Yes")
else:
    print("No")
