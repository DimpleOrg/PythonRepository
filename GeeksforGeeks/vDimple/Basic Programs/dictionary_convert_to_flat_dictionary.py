# -*- coding: utf-8 -*-
"""
Created on Sat May 29 08:19:36 2021

@author: dimpl
"""

# Convert key-values list to flat dictionary
test_dict = {"month": [1, 2, 3], "name": ["Jan", "Feb", "March"]}
res = dict(zip(test_dict["month"], test_dict["name"]))
print(res)
