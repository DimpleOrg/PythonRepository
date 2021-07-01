# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:28:10 2021

@author: dimpl
"""

# Given a string and a number k, find the k-th non-repeating character in the string. Consider a large input string with lacs of characters and a small character set. How to find the character by only doing only one traversal of input string?
# Examples:
# Input : str = geeksforgeeks, k = 3
# Output : r
# First non-repeating character is f, second is o and third is r.

from collections import OrderedDict

str = "geeksforgeeks"
k = 3
ctr = "First"
dict_a = OrderedDict.fromkeys(str, 0)

for ch in str:
    dict_a[ch] += 1

while k > 0:
    for key, val in dict_a.items():
        if val < 2:
            print(ctr, " non repeating character is ", key)
            ctr = "Second"
            k -= 1
