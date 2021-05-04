# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 17:09:09 2021

@author: dimpl
"""

# Adding and Subtracting Matrices in Python

# Example:
# A = [[1,2],[3,4]]
# B = [[4,5],[6,7]]

# then we get
# A+B = [[5,7],[9,11]]
# A-B = [[-3,-3],[-3,-3]]

A = [[1, 2], [3, 4]]
B = [[4, 5], [6, 7]]

import numpy as np

A1 = np.array(A)
B1 = np.array(B)
res = np.add(A1, B1)
print("Addition: ", res)
res = np.subtract(A1, B1)
print("Subtraction: ", res)
