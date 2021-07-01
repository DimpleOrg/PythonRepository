# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 06:35:04 2021

@author: dimpl
"""

# Python – Adding Tuple to List and vice – versa
test_list = [5, 6, 7]

# initializing tuple
test_tup = (9, 10)

# Adding Tuple to List and vice - versa
# Using += operator (list + tuple)
test_list += test_tup

# printing result
print("The container after addition : " + str(test_list))


print("***************************************************")
# Method #2 : Using tuple(), data type conversion [tuple + list]

test_list = [5, 6, 7]
test_tup = (9, 10)

res_tuple = tuple(list(test_tup) + test_list)
print(res_tuple)
