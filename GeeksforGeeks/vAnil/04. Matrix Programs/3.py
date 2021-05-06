# -*- coding: utf-8 -*-
"""
Created on Mon May  3 04:14:32 2021

@author: ANIL
"""

'''
Getting the product of list is quite common problem and has been dealt with and discussed many times, but sometimes, we require to better it and total product, i.e. including those of nested list as well. Let’s try and get the total product and solve this particular problem.
'''

test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]


temp_list = [ val  for listItem in test_list for val in listItem]

result = 1
for item in temp_list:
    result *= item


print(result)