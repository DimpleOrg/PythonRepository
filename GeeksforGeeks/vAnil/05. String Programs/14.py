# -*- coding: utf-8 -*-
"""
Created on Sun May  9 09:47:35 2021

@author: ANIL
"""

'''
Python | Maximum frequency character in String
'''

test_str = "GeeksforGeeks"

charDic = {}

for ch in test_str:
    if ch in charDic.keys():
        charDic[ch] += 1
    else:
        charDic[ch] = 0
        
minCh = max(charDic, key=charDic.get)

print('max fequency char is:',minCh)