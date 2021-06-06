# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 16:11:31 2021

@author: ANIL
"""

'''
Python – Sort Dictionary key and values List
Input : test_dict = {‘c’: [3], ‘b’: [12, 10], ‘a’: [19, 4]}
Output : {‘a’: [4, 19], ‘b’: [10, 12], ‘c’: [3]}

Input : test_dict = {‘c’: [10, 34, 3]}
Output : {‘c’: [3, 10, 34]}
'''
test_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

test_dict = sorted(map(lambda x: (x[0],sorted(x[1])),test_dict.items()) )
print(test_dict)