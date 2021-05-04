# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 08:58:54 2021

@author: dimpl
"""
# Python | Matrix creation of n*n

# Method 1
n = 4
list_n1 = [[0] * n] * n
print(list_n1)


# Method 2:
res = [list(range(x + 1, x + n + 1)) for x in range(n)]
res1 = [list(range(1 + n * x, 1 + n * (x + 1))) for x in range(n)]
print(f"\n{res}")
print("\n", res1)


# Method 3 : Using next() + itertools.count()
import itertools

temp = itertools.count(1)
res3 = [[next(temp) for i in range(n)] for i in range(n)]
print("\n", res3)
