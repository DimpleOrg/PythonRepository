# -*- coding: utf-8 -*-
"""
Created on Tue May  4 04:34:29 2021

@author: ANIL
"""

'''
Ways to remove i’th character from string in Python
'''

s = 'abcdefgh'

t = 4  # 4th char is 'd'

ans = s[:t-1] + s[t:]

print(ans)