# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 17:19:16 2021

@author: dimpl
"""

# =============================================================================
# Given two matrix the task is that we will have to create a program to multiply two matrices in python.
#
# Examples:
#
# Input : X = [[1, 7, 3],
#              [3, 5, 6],
#              [6, 8, 9]]
#        Y = [[1, 1, 1, 2],
#            [6, 7, 3, 0],
#            [4, 5, 9, 1]]
#
# Output : [55, 65, 49, 5]
#          [57, 68, 72, 12]
#          [90, 107, 111, 21]
# =============================================================================

X = [[1, 7, 3], [3, 5, 6], [6, 8, 9]]
Y = [[1, 1, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

# METHOD 1- Using Numpy
import numpy as np

result = np.dot(X, Y)
print(result)


# METHOD 2- Using Simple Nested Loops
res1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# iterating by row of A
for i in range(len(X)):

    # iterating by coloum by B
    for j in range(len(Y[0])):

        # iterating by rows of B
        for k in range(len(Y)):
            res1[i][j] += X[i][k] * Y[k][j]
print("\n", res1)


# Alternate way for Mathod 2
res3 = []
# iterating by row of A

for i in range(len(X)):
    temp_list = []

    # iterating by coloum by B
    for j in range(len(Y[0])):
        temp = 0

        # iterating by rows of B
        for k in range(len(Y)):
            temp += X[i][k] * Y[k][j]
        temp_list.append(temp)
    res3.append(temp_list)

print("\nRes3: ", res3)


# Method 3: Matrix Multiplication Using List Comprehension

res2 = [[sum(x * y for x, y in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
print("\n", res2)

# =============================================================================
# To explain the zip(*Y) using the example values:
# let
# Y = [[5, 1],
#      [2, 1]]
# the * will make it expand the top-level list to a number of separate arguments
#
# zip([5, 1], [2, 1])
# And the zip will then yield a sequence of tuples consisting of the first element from each input list, then the second element of each input list (and so on, although in this case there are only two pairs), i.e.
#
# (5, 2)
# (1, 1)
# In other words, the columns of Y.
# =============================================================================
