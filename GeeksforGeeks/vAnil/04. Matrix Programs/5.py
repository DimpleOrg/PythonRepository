# -*- coding: utf-8 -*-
"""
Created on Mon May  3 04:28:23 2021

@author: ANIL
"""

'''
Transpose a matrix in Single line in Python
'''

m = [[1,2],[3,4],[5,6]]

trans = [ list(item) for item in zip(*m)]

print(trans)