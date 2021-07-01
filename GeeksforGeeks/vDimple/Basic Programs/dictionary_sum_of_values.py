# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:35:12 2021

@author: dimpl
"""

# Python program to find the sum of all items in a dictionary
# Input : {'a': 100, 'b':200, 'c':300}
# Output : 600

# Input : {'x': 25, 'y':18, 'z':45}
# Output : 88

dict_a = {"a": 100, "b": 200, "c": 300}
res = sum(dict_a.values())
print(res)
