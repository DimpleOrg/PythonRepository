# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:14:16 2021

@author: ANIL
"""

'''
Python | Sort Python Dictionaries by Key or Value

'''

test_dict = {'c': 3,'b': 12, 'a': 19}
#sort by key
test_dict = sorted(test_dict.items(), key = lambda x:x[0])
print(test_dict)


#sort by key
test_dict = {'c': 31,'b': 12, 'a': 19}
test_dict = sorted(test_dict.items(), key = lambda x: x[1])
print(test_dict) 


#sort by key,value
test_dict = {'c': 31,'b': 12, 'a': 19}
test_dict = sorted(test_dict.items(), key = lambda x: (x[0],x[1]))
print(test_dict) 
