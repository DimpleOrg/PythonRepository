# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 01:03:42 2021

@author: dimpl
"""

# Python Program for Sum of squares of first n natural numbers
# Input : N = 4
# Output : 30
# 1^2 + 2^2 + 3^2 + 4^2
# = 1 + 4 + 9 + 16
# = 30

# Input : N = 5
# Output : 55

import math

n = 4
sum_of_squares = []
if len(sum_of_squares) >= n:
    print(sum_of_squares[n])
else:
    last_known = len(sum_of_squares)+1
    sum = 0
    for i in range(last_known, n+1):
        sum += i**2
        sum_of_squares.append(sum)
    print(sum_of_squares[-1])

# -----------------------METHOD 2-------------------------------

#n = 4
print(n*(n+1)*((2*n)+1)/6)
