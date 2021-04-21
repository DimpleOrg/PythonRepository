# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 12:15:33 2021

@author: dimpl
"""

# Sort the values of first list using second list in Python

# Input : list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
#         list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

# Output :['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']

# Input : list1 = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
#         list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

# Output : ['g', 'k', 'r', 'e', 'e', 'g', 's', 'f', 'o']


list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
zipped_pairs = zip(list2, list1)
res = [x for _, x in sorted(zipped_pairs)]
print(res)
