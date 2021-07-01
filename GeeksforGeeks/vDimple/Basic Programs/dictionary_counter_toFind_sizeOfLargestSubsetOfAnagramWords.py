# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:12:08 2021

@author: dimpl
"""

# Given an array of n string containing lowercase letters. Find the size of largest subset
# of string which are anagram of each others. An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc” are anagram of each other.

# Examples:

# Input:
# ant magenta magnate tan gnamate
# Output: 3
# Explanation
# Anagram strings(1) - ant, tan
# Anagram strings(2) - magenta, magnate,
#                      gnamate
# Thus, only second subset have largest
# size i.e., 3

arr = ["ant", "magenta", "magnate", "tan", "gnamate"]
dict_a = {}
for each in arr:
    sorted_each = "".join(sorted(each))
    if sorted_each in dict_a.keys():
        dict_a[sorted_each].append(each)
    else:
        dict_a[sorted_each] = [each]

max_key = ""
max_val = 0
for key, val in dict_a.items():
    if max_val < len(val):
        max_val = len(val)
        max_key = key

print(dict_a[key])
print(len(dict_a[key]))


# ****************METHOD 2: ************
from collections import Counter

arr1 = "ant magenta magnate tan gnamate"
arr1 = arr1.split()
for i in range(0, len(arr)):
    arr1[i] = "".join(sorted(arr1[i]))

res_dict = Counter(arr1)
print(max(res_dict.values()))
