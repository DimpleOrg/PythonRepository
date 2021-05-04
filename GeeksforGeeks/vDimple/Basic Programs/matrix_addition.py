# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 19:33:06 2021

@author: dimpl
"""

X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[sum(x) for x in zip(*t)] for t in zip(X, Y)]

print(result)


# Matrix Subtraction
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[x - y for x, y in zip(*t)] for t in zip(X, Y)]

print(result)
