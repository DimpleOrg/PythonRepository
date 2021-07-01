# -*- coding: utf-8 -*-
"""
Created on Sat May 29 08:23:11 2021

@author: dimpl
"""

# Insertion at the beginning in OrderedDict
# Input:
# original_dict = {'a':1, 'b':2}
# item to be inserted ('c', 3)

# Output:  {'c':3, 'a':1, 'b':2}

# Method #1: Using OrderedDict.move_to_end()
from collections import OrderedDict

unordered_dict = OrderedDict([("akshat", "1"), ("nikhil", "2")])
unordered_dict.update({"manjeet": "3"})
unordered_dict.move_to_end("manjeet", last=False)
print(unordered_dict)


# Method #2: Using Naive Approach
# This method only works in case of unique keys

from collections import OrderedDict

# initialising ordered_dict
ini_dict1 = OrderedDict([("akshat", "1"), ("nikhil", "2")])
ini_dict2 = OrderedDict([("manjeet", "4"), ("akash", "4")])

# adding in beginning of dict
both = OrderedDict(list(ini_dict1.items()) + list(ini_dict2.items()))
print(both)
