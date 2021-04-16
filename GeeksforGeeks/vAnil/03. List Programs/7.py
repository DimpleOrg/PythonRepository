# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:24:54 2021

@author: ANIL
"""

'''
Given a list of numbers, write a Python program to find the sum of all the elements in the list.
Example: 
 

Input: [12, 15, 3, 10]
Output: 40

Input: [17, 5, 3, 5]
Output: 30
'''

input_list = [12, 15, 3, 10]

print(sum(input_list))

list_sum = 0

for val in input_list:
    list_sum += val
    
print(list_sum)