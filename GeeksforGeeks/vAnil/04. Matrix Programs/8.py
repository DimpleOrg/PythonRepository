# -*- coding: utf-8 -*-
"""
Created on Mon May  3 04:37:27 2021

@author: ANIL
"""

'''
Python – Vertical Concatenation in Matrix
'''
from itertools import zip_longest
test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]

concat = ["".join(ele) for ele in zip_longest(*test_list, fillvalue ="")]

print(concat)