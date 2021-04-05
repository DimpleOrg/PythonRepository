# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:44:53 2021

@author: ANIL
"""

def factorial(num):
    result = 1
    for i in range(1,num+1):
        result = result * i
    
    return result


print(factorial(1024))
        