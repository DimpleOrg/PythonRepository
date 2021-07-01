# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:31:53 2021

@author: dimpl
"""

# Extract Unique values dictionary values
# The original dictionary is : {‘gfg’: [5, 6, 7, 8],
#                               ‘best’: [6, 12, 10, 8],
#                               ‘is’: [10, 11, 7, 5],
#                               ‘for’: [1, 2, 5]}
# The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]

test_dict = {
    "gfg": [5, 6, 7, 8],
    "is": [10, 11, 7, 5],
    "best": [6, 12, 10, 8],
    "for": [1, 2, 5],
}
res = set([each for val in test_dict.values() for each in val])
print(res)


# ************************************************************
# Method 2: using chain()
from itertools import chain

test_dict = {
    "gfg": [5, 6, 7, 8],
    "is": [10, 11, 7, 5],
    "best": [6, 12, 10, 8],
    "for": [1, 2, 5],
}
res = set(chain(*test_dict.values()))
print(res)
