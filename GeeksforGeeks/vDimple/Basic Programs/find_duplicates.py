# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:20:06 2021

@author: dimpl
"""

# Python | Program to print duplicates from a list of integers

# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]


# Input :  list = [-1, 1, -1, 8]
# Output : output_list = [-1]

# list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
list2 = [-1, 1, -1, 8]
res_set1=set()
dup_set2=set()
for x in list2:
    if x in res_set1:
        dup_set2.add(x)
    else:
        res_set1.add(x)
        
print(list(dup_set2))
        
    