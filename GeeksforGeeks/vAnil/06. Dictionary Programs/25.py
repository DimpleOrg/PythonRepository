# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:39:49 2021

@author: ANIL
"""

'''
Python dictionary, set and counter to check if frequencies can become same

Given a string which contains lower alphabetic characters, we need to remove
at most one character from this string in such a way that frequency of each 
distinct character becomes same in the string.

'''
from collections import Counter

string = 'xxxxyyzz'
dic = Counter(string)

count = list(set(dic.values()))

if len(count) > 2 or (len(count)==2 and count[0]==count[1]):
    print('False')
else:
    print('True')