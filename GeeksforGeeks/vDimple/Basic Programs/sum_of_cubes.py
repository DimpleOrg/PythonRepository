# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 20:48:24 2021

@author: dimpl
"""

# Program for cube sum of first n natural numbers
# Examples:

# Input : n = 5
# Output : 225
# 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225

# Input : n = 7
# Output : 784
# 1^3 + 2^3 + 3^3 + 4^3 + 5^3 +
# 6^3 + 7^3 = 784

import math

n = 3
sum_of_cubes = []
if len(sum_of_cubes) >= n:
    print(sum_of_cubes[n])
else:
    last_known = len(sum_of_cubes)+1
    sum = 0
    for i in range(last_known, n+1):
        sum += i**3
        sum_of_cubes.append(sum)
    print(sum_of_cubes[-1])

# -----------------------METHOD 2-------------------------------

#n = 3
print(pow(n*(n+1)/2, 2))
