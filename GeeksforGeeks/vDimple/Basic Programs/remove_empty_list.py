# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 07:23:48 2021

@author: dimpl
"""

# Python – Remove empty List from List

# Method #1 : Using list comprehension
list1 = [5, 6, [], 3, [], [], 9]
list1=[x for x in list1 if x]
print(list1)

# Method #2 : Using filter()
list1= [5, 6, [], 3, [], [], 9]
res=list(filter(None,list1))
print(res)

