# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 22:52:51 2021

@author: dimpl
"""

# Python program to sort a list of tuples by second Item

# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)]
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]


# Method #1: Using sorted() method
test_list = [("for", 24), ("Geeks", 8), ("Geeks", 30)]
res = sorted(test_list, key=lambda x: x[1])
print(res)

# Method #2: Using sort() method
test_list.sort(key=lambda x: x[1])
print(test_list)
