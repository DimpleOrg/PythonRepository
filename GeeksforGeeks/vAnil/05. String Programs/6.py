# -*- coding: utf-8 -*-
"""
Created on Tue May  4 04:53:45 2021

@author: ANIL
"""

'''
Python – Words Frequency in String Shorthands
'''

from collections import Counter

s = 'hellow world how are you . you are the best and world is waiting'

words = s.split()

result = Counter(words)

print(result)