# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 07:06:47 2021

@author: dimpl
"""

# =============================================================================
# Given a list of numbers, write a Python program to remove multiple elements 
# from a list based on the given condition.
# 
# =============================================================================


# Let’s say we want to delete each element in the list which is divisible by 2 or all the even numbers.
list1=[12, 15, 3, 10]
list1=[x for x in list1 if x%2!=0]
print(list1)


# Input: [12, 15, 3, 10]
# Given Condition: Remove = [12, 3], New_List = [15, 10]

list1=[12, 15, 3, 10]
unwanted_num = [12, 3]
list1=[x for x in list1 if x not in unwanted_num]
print(list1)


# Input: [11, 5, 17, 18, 23, 50]
# Given Condition: Remove = [1:5], New_list = [11, 50]

list1=[11, 5, 17, 18, 23, 50]
del list1[1:5]
print(list1)


# When index of elements is known.
list1 = [11, 5, 17, 18, 23, 50] 
  
# given index of elements 
# removes 11, 18, 23
unwanted = [0, 3, 4]
for each in sorted(unwanted,reverse=True):
    del list1[each]
print(*list1)