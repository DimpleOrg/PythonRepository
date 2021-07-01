# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:24:17 2021

@author: dimpl
"""

# Counting the frequencies in a list using dictionary in Python

# Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
#                   4, 4, 4, 2, 2, 2, 2]
# Output : 1 : 5
#          2 : 4
#          3 : 3
#          4 : 3
#          5 : 2

from collections import Counter

list_in = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
res = Counter(list_in)
for each in res:
    print(each, res[each])
