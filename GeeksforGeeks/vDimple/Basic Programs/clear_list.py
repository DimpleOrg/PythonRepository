# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 00:24:32 2021

@author: dimpl
"""

# Different ways to clear a list in Python

# Method #1 : Using clear() method
my_list = [6, 0, 4, 1]
print(my_list)
my_list.clear()
print(my_list)

# Method #2 : Reinitializing the list
my_list = [6, 0, 4, 1]
print(my_list)
my_list = []
print(my_list)

# Method #4 : Using del
my_list = [6, 0, 4, 1]
print(my_list)
del my_list[:]
print(my_list)
