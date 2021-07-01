# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 22:21:46 2021

@author: dimpl
"""

# Convert Nested Tuple to Custom Key Dictionary
# Input : test_tuple = ((1, ‘Gfg’, 2), (3, ‘best’, 4)), keys = [‘key’, ‘value’, ‘id’]
# Output : [{‘key’: 1, ‘value’: ‘Gfg’, ‘id’: 2}, {‘key’: 3, ‘value’: ‘best’, ‘id’: 4}]

test_tuple = ((1, "Gfg", 2), (3, "best", 4))
keys = ["key", "value", "id"]

res = [{"key": sub[0], "value": sub[1], "id": sub[2]} for sub in test_tuple]
print(res)


# Method #2 : Using zip() + list comprehension
res1 = [{key: val for key, val in zip(keys, sub)} for sub in test_tuple]
print(res1)
