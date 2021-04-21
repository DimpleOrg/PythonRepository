# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:06:28 2021

@author: ANIL
"""

'''
Given a list of integers with duplicate elements in it. The task to generate another list, which contains only the duplicate elements. In simple words, the new list should contain the elements which appear more than one.

Examples :

Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]


Input :  list = [-1, 1, -1, 8]
Output : output_list = [-1]
'''

list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

set1 = set()

set2 = set()

list2 = [list1[0]]

for item in list1:
    if item not in set1:
        set1.add(item)
    else:
        set2.add(item)

print(set2)


