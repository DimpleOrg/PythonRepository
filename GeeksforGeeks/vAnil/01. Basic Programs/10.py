# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:18:50 2021

@author: ANIL
"""

def printNthFib(n):
    fibSeries = [0,1]
    
    for i in range(2,n):
        fibSeries.append(fibSeries[i-1]+fibSeries[i-2])
        
    return fibSeries[n-1]


print(printNthFib(19))