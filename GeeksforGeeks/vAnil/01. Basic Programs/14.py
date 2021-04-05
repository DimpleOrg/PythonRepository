# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:16:13 2021

@author: ANIL
"""
'''
Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.

Examples:

Input : N = 4
Output : 30
12 + 22 + 32 + 42
= 1 + 4 + 9 + 16
= 30

Input : N = 5
Output : 55
'''

n = int(input('Please enter the value of N:'))
sum = 0

for i in range(1,n+1):
    sum += i**2
    
print( f'Value of sum of squares 1^2 + 2^2 + 3^2 + ….. + N^2: {sum}')
