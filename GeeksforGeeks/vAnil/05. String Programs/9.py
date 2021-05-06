# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:26:22 2021

@author: ANIL
"""

'''
Python program to print even length words in a string

Input: s = "This is a python language"
Output: This
        is
        python
        language 
'''

s = "i am Anil"

words = s.split()

for word in words:
    if (len(word)%2==0):
        print(word)
        
        
