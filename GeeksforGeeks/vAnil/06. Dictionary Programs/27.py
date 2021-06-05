# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:03:00 2021

@author: ANIL
"""

'''
Possible Words using given characters in Python

Given a dictionary and a character array, 
print all valid words that are possible using characters from the array.
'''

dic = ["go","bat","me","eat","goal","boy", "run"]

arr = ['e','o','b', 'a','m','g', 'l']

setArr = set(arr)

for word in dic:
    dsec = set(word)
    
    if dsec & setArr == dsec:
        print(word)
