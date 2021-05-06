# -*- coding: utf-8 -*-
"""
Created on Mon May  3 04:22:28 2021

@author: ANIL
"""

'''
Adding and Subtracting Matrices in Python


Suppose we have two matrices A and B.
A = [[1,2],[3,4]]
B = [[4,5],[6,7]]

then we get
A+B = [[5,7],[9,11]]
A-B = [[-3,-3],[-3,-3]]


''' 

import numpy as np
  
  
A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 5], [6, 7]])
  
print(A)

print(B)
  
print("Addition of two matrix")
print(np.add(A, B))

print("Subtraction of two matrix")
print(np.subtract(A, B))

