# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 00:33:23 2021

@author: dimpl
"""
# Reversing a List in Python

my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)

# ---------------METHOD 2-------------
my_list = [1, 2, 3, 4]
ctr = 0
length = len(my_list)-1

while ctr < (len(my_list)//2):
    temp = my_list[ctr]
    my_list[ctr] = my_list[length-ctr]
    my_list[length-ctr] = temp
    ctr += 1

print(my_list)


# -------------------METHOD 3----------------------
# Method 3: Using the slicing technique.

my_list = [1, 2, 3, 4]
new_lst = my_list[::-1]
print(new_lst)
