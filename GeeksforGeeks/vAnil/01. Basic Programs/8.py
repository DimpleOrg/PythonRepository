# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:01:14 2021

@author: ANIL
"""

def printAllPrime(min,max):
    primeNums = [2]
    
    if min < 2:
        print(2)
    
    for i in range(3,max+1):
        flag = True
        for prime in primeNums:
            if i%prime == 0:
                flag = False
                break
        if flag:
            primeNums.append(i)
            
            if i >= min:
                print(i)
            
            
            

printAllPrime(10, 20)