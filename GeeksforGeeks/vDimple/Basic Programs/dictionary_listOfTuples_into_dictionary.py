# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:28:25 2021

@author: dimpl
"""

# Convert a list of Tuples into Dictionary
# Input : [('A', 1), ('B', 2), ('C', 3)]
# Output : {'B': [2], 'A': [1], 'C': [3]}

list_a = [("A", 1), ("B", 2), ("C", 3), ("C", 13)]
dict_a = {}
for each in list_a:
    if each[0] in dict_a.keys():
        dict_a[each[0]].append(each[1])
    else:
        dict_a.setdefault(each[0], []).append(each[1])
print(dict_a)
