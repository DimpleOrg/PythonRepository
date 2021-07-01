# -*- coding: utf-8 -*-
"""
Created on Sun May 30 23:34:32 2021

@author: dimpl
"""

# Sort Dictionary key and values List
# Input : test_dict = {‘c’: [3], ‘b’: [12, 10], ‘a’: [19, 4]}
# Output : {‘a’: [4, 19], ‘b’: [10, 12], ‘c’: [3]}

test_dict = {"c": [3], "b": [12, 10], "a": [19, 4]}

for key in test_dict:
    test_dict[key] = sorted(test_dict[key])


print(sorted(test_dict.items()))
