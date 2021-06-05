# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 08:16:03 2021

@author: ANIL
"""

'''
Python program to create a list of tuples from given list having number 
and its cube in each tuple
'''

x = [1, 2, 3]

tuples = [(item, item**3) for item in x]

print(tuples)