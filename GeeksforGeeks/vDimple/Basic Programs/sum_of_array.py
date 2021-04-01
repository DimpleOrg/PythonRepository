# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 22:44:50 2021

@author: dimpl
"""

# Python Program to find sum of array
# Input : arr[] = {1, 2, 3}
# Output : 6
# 1 + 2 + 3 = 6

# Input : arr[] = {15, 12, 13, 10}
# Output : 50

# input values to list
arr = [12, 3, 4, 15]

# sum() is an inbuilt function in python that adds
# all the elements in list,set and tuples and returns
# the value
ans = sum(arr)
print(ans)

# ----------------------------METHOD 2------------------------------
sum = 0
for i in arr:
    sum += i
print(sum)
