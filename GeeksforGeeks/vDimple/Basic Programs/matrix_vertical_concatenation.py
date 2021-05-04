# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:29:23 2021

@author: dimpl
"""

# Given a String Matrix, perform column-wise concatenation of strings, handling variable lists lengths.

# Input : [[“Gfg”, “good”], [“is”, “for”]]
# Output : [‘Gfgis’, ‘goodfor’]
# Explanation : Column wise concatenated Strings, “Gfg” concatenated with “is”, and so on.

# Input : [[“Gfg”, “good”, “geeks”], [“is”, “for”, “best”]]
# Output : [‘Gfgis’, ‘goodfor’, “geeksbest”]
# Explanation : Column wise concatenated Strings, “Gfg” concatenated with “is”, and so on.

from itertools import zip_longest

list1 = [["Gfg", "good"], ["is"]]
res = ["".join(x) for x in zip_longest(*list1, fillvalue="")]
print(res)
