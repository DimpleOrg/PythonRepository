# -*- coding: utf-8 -*-
"""
Created on Sun May  9 09:56:58 2021

@author: ANIL
"""

'''
Python program for removing i-th character from a string

Input : Geek
        i = 1
Output : Gek 
'''

string = "geeksFORgeeks"
i = 5

result = string[:i] + string[i+1:]

print(result)

