# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:06:40 2021

@author: ANIL
"""

'''
The problem of finding summation of digit of number is quite common. This can sometimes come in form of list and we need to perform that. This has application in many domains such as school programming and web development. Let’s discuss certain ways in which this problem can be solved.
'''

def sumOfDigit(x):
    sumdigit = 0
    while(x>0):
        sumdigit += (x%10)
        x = x//10
        
    return sumdigit

        


test_list = [12, 67, 98, 34]
sum_list = []

for item in test_list:
    sum_list.append(sumOfDigit(item))
    
print(sum_list)