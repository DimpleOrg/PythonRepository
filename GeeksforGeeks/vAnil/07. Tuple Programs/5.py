# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 08:27:05 2021

@author: ANIL
"""
'''
Python – Closest Pair to Kth index element in Tuple
'''

test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]

tup = (17, 23)

k = 2

index = 0
min_diff = abs(tup[k-1]-test_list[0][k-1]) 

resutl = (test_list[0])
for i,item in enumerate(test_list):
    diff = abs(tup[k-1]-item[k-1])
    if diff < min_diff:
        index=i
        min_diff= diff


print(test_list[i])        