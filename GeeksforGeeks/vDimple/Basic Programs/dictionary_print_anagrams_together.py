# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:36:37 2021

@author: dimpl
"""

# Print anagrams together in Python using List and Dictionary

# Input : arr = ['cat', 'dog', 'tac', 'god', 'act']
# Output : 'cat tac act dog god'

arr = ["cat", "dog", "tac", "god", "act"]
dict_a = {}
for each in arr:
    sorted_each = "".join(sorted(each))
    if sorted_each in dict_a.keys():
        dict_a[sorted_each].append(each)
    else:
        dict_a[sorted_each] = [each]

for val in dict_a.values():
    print(val)
