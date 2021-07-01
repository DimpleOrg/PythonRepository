# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 22:52:51 2021

@author: dimpl
"""

# Remove Tuples of Length K
# Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2
# Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
# Explanation : (4, 5) of len = 2 is removed.


test_list = [(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7)]
K = 2

res = [each for each in test_list if len(each) != K]
print(res)


# Method #2 : Using filter() + lambda + len()

res1 = list(
    filter(lambda x: len(x) != K, test_list)
)  # when should we typecast list() and when [] works?
print(res1)
