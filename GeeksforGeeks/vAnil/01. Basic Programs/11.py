# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:29:16 2021

@author: ANIL
"""

def isPerfectSquare(num):
    if num==1:
        return True
    else:
        i = 2
        while i*i <= num:
            if i*i == num:
                return True
            i += 1
            
    return False


def isFibNum(n):
    if isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4):
        return True
    
    return False


print(isFibNum(2584))
print(isFibNum(2584))