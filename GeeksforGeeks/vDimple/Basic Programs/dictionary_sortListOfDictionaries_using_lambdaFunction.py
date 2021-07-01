# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:16:42 2021

@author: dimpl
"""

# Ways to sort list of dictionaries by values in Python – Using lambda function
lis = [
    {"name": "Nandini", "age": 20},
    {"name": "Manjeet", "age": 20},
    {"name": "Nikhil", "age": 19},
]

print(sorted(lis, key=lambda i: i["age"]))
print(sorted(lis, key=lambda i: (i["age"], i["name"])))
print(sorted(lis, key=lambda i: i["age"], reverse=True))
