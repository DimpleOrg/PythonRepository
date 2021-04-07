# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:29:55 2021

@author: ANIL
"""

'''
Given a list, print the value obtained after multiplying all numbers in a list. 
Examples: 
 

Input :  list1 = [1, 2, 3] 
Output : 6 
Explanation: 1*2*3=6 

Input : list1 = [3, 2, 4] 
Output : 24 
'''
import numpy

input_list = [12, 15, 3, 10]

print(numpy.prod(input_list))

list_prod = 1

for val in input_list:
    list_prod *= val
    
print(list_prod)