# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:48:28 2021

@author: dimpl
"""

# Ways to sort list of dictionaries by values in Python – Using itemgetter

# Itemgetter- It takes keys of dictionaries and converts them into tuples.
# It reduces overhead and is faster and more efficient. The “operator” module has
#  to be imported for its working.

from operator import itemgetter

lis = [
    {"name": "Nandini", "age": 20},
    {"name": "Manjeet", "age": 20},
    {"name": "Nikhil", "age": 19},
]

print(sorted(lis, key=itemgetter("age")))
print(sorted(lis, key=itemgetter("age", "name")))
print(sorted(lis, key=itemgetter("age"), reverse=True))


# =============================================================================
# Advantages of itemgetter over lambda
# Performance : itemgetter performs better than lambda functions in the context of time.
# Concise : : itemgetter looks more concise when accessing multiple values than lambda
# functions.
# =============================================================================
