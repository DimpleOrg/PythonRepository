# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 00:19:58 2021

@author: dimpl
"""

# Ways to find length of list

my_list = [1, 2, 3, 4]
print(len(my_list))

# --------------------METHOD2-----------------
ctr = 0
for i in my_list:
    ctr += 1
print(ctr)
