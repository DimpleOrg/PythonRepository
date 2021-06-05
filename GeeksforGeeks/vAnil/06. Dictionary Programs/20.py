# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:48:33 2021

@author: ANIL
"""

'''
Python | Remove all duplicates words from a given sentence
'''

inp = 'Python is great and Java is also great'
inp = inp.split()

print(*set(inp))