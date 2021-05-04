# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 08:54:01 2021

@author: dimpl
"""

m = [[1, 2], [4, 5], [3, 6]]
res = [list(n) for n in zip(*m)]
print(res)


# Method 2
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print(rez)


# Method 3: Using numpy
import numpy as np

m = np.array(m)
print("\n")
print(np.transpose(m))
# or
print(m.T)
