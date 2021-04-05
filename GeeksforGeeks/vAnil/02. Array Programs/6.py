# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:04:10 2021

@author: ANIL
"""

'''
Given multiple numbers and a number n, the task is to print the remainder after multiply all the number divide by n.
Examples: 

Input : arr[] = {100, 10, 5, 25, 35, 14}, 
            n = 11
Output : 9
100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9
'''

arr = [100, 10, 5, 25, 35, 14]
n = 11

answer = 1

for val in arr:
    answer *= val%n
    
print(answer%11)
    
