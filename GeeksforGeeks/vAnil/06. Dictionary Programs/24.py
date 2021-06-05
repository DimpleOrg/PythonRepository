# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:31:23 2021

@author: ANIL
"""

'''
Python counter and dictionary intersection example
(Make a string using deletion and rearrangement)

Given two strings, find if we can make first string from second by deleting 
some characters from second and rearranging remaining characters.

'''
from collections import Counter

s1 = 'ABHISHEKsinGH'
s2 = 'gfhfBHkooIHnfndSHEKsiAnG'

dic1 = Counter(s1)
dic2 = Counter(s2)


result = dic1 & dic2

if dic1 == result:
    print('POSSIBLE')
else:
    print('NOT POSSIBLE')
    