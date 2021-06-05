# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:25:56 2021

@author: ANIL
"""

'''
K’th Non-repeating Character in Python using List Comprehension and OrderedDict
'''
from collections import OrderedDict 

x = "geeksforgeeks"
k = 3

dic=OrderedDict()

for ch in x:
    if ch in dic:
        dic[ch] += 1
    else:
        dic[ch]=1

freqOneList = [ch for ch in dic if dic[ch]==1]


if k <= len(freqOneList):
    print(freqOneList[k-1])
else:
    print('Not found')
