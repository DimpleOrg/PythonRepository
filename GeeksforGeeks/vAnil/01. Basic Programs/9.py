# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:10:53 2021

@author: ANIL
"""

def IsPrime(num):
    if num<=1:
        print('Invalid input')
        return
    
    for i in range(2,num):
        if num < (i*i):
            if num%i==0:
                return False
            
    return True



print(IsPrime(101))