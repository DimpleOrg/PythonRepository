# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 06:39:08 2021

@author: dimpl
"""

# Python – Closest Pair to Kth index element in Tuple
# Input :
# test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
# tup = (17, 23)
# K = 2
# Output : (19, 23)

# Input :
# test_list = [(3, 4, 9), (5, 6, 7)]
# tup = (1, 2, 5)
# K = 3
# Output : (5, 6, 7)


test_list = [(3, 4, 9), (5, 6, 9)]
listOfTestList = [
    each for each in test_list
]  # how to create a list without 2 for loops

tup = (1, 2, 5)
K = 3

min_diff = abs(tup[0] - test_list[0][0])
res = None

for index, val in enumerate(test_list):
    for each in val:
        dif = abs(tup[K - 1] - each)
        if dif < min_diff:
            min_diff = dif
            res = index

print(test_list[res])
