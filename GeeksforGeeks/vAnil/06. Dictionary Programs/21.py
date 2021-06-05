# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:08:41 2021

@author: ANIL
"""

'''
Python Dictionary to find mirror characters in a string
'''

string = 'paradox'
n = 3

prefix = string[:n-1]
mirChars = string[n-1:]

suffix = ''
for ch in mirChars:
    d = ord(ch) - ord('a')
    suffix += chr(ord('z') - d)

print( f"output: {prefix+suffix}")