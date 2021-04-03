# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:20:55 2021

@author: ANIL
"""

'''
Print the sum of series 13 + 23 + 33 + 43 + …….+ n3 till n-th term.

Examples:

Input : n = 5
Output : 225
13 + 23 + 33 + 43 + 53 = 225

Input : n = 7
Output : 784
13 + 23 + 33 + 43 + 53 + 
63 + 73 = 784
'''

n = int(input('Please enter the value of N:'))
sum = 0

for i in range(1,n+1):
    sum += i**3
    
print( f'Value of sum of cubes 1^3 + 2^3 + 3^3 + ….. + N^3: {sum}')
