# -*- coding: utf-8 -*-
"""
Created on Sun May 30 13:35:50 2021

@author: ANIL
"""

'''
Given a string, find all the duplicate characters which are similar to each others.

Let’s look at the example.
Examples:

Input : hello
Output : l

Input : geeksforgeeeks
Output : e g k s
'''
from collections import Counter
in_str = 'geeksforgeeks'

dic = Counter(in_str)

for key,value in dic.items():
    if (value > 1):
        print(key,end=' ')

