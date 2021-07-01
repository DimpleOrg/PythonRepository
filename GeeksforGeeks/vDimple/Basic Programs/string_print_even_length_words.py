# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:47:38 2021

@author: dimpl
"""

# Python program to print even length words in a string

s = "This is a python language"
res = [word for word in s.split() if len(word) % 2 == 0]
print(res)
