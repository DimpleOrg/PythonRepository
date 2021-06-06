# -*- coding: utf-8 -*-
"""
Created on Sun May  9 09:39:59 2021

@author: ANIL
"""

'''
Python – Least Frequent Character in String
'''


test_str = "GeeksforGeeks"

charDic = {}

for ch in test_str:
    if ch in charDic.keys():
        charDic[ch] += 1
    else:
        charDic[ch] = 0
        
minCh = min(charDic, key=charDic.get)

print('min fequency char is:',minCh)