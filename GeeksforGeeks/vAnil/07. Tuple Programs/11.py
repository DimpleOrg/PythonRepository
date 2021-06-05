# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:47:11 2021

@author: ANIL
"""

'''
Python – Order Tuples by List
'''

# initializing list
test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]

# printing original list
print("The original list is : " + str(test_list))

# initializing order list
ord_list = ['Geeks', 'best', 'CS', 'Gfg']

# Order Tuples by List
# Using dict() + list comprehension
temp = dict(test_list)
res = [(key, temp[key]) for key in ord_list]

# printing result
print("The ordered tuple list : " + str(res))
