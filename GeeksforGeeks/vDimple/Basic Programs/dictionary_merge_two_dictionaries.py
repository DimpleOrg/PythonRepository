# -*- coding: utf-8 -*-
"""
Created on Sat May 29 08:15:11 2021

@author: dimpl
"""

# Merging two Dictionaries

dict1 = {"a": 10, "b": 8}
dict2 = {"d": 6, "c": 4}

# This return None
print(dict2.update(dict1))


# changes made in dict2
print(dict2)


# Method 2: **
# ** implies that an argument is a dictionary. Using ** [double star] is a shortcut
# that allows you to pass multiple arguments to a function directly using a dictionary.
# For more information refer **kwargs in Python. Using this we first pass all the
# elements of the first dictionary into the third one and then pass the second dictionary
# into the third. This will replace the duplicate keys of the first dictionary.

dict1 = {"a": 10, "b": 8}
dict2 = {"d": 6, "c": 4}
dict3 = {**dict1, **dict2}
print(dict3)
