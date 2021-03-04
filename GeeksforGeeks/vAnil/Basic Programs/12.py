# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:02:40 2021

@author: ANIL
"""


fibSeries = [1,1]

def printNthFib(n):

    if n <= len(fibSeries):
        return fibSeries[n-1]
    
    for i in range(len(fibSeries),n):
        fibSeries.append(fibSeries[i-1]+fibSeries[i-2])
        
    return fibSeries[n-1]


def nth_multiple_fib(k,n):
    count = 0
    result = 0
    i = 1
    while count < n:
        result = printNthFib(i)
        if result % k == 0:
            count += 1
        i += 1
        
    return i-1


def efficient_nth_multiple_fib(k,n):
    count = 0
    result = 0
    i = 1
    while count < n:
        result = printNthFib(i)
        if result % k == 0:
            break
        i += 1
        
    return i*n



k,n = 2,3
print(f'{n} mulitple of {k} is at index:', nth_multiple_fib(k, n))
k,n = 4,5
print(f'{n} mulitple of {k} is at index:', nth_multiple_fib(k, n))

k,n = 2,3
print(f'{n} mulitple of {k} is at index:', efficient_nth_multiple_fib(k, n))
k,n = 4,5
print(f'{n} mulitple of {k} is at index:', efficient_nth_multiple_fib(k, n))


    