# -*- coding: utf-8 -*-
"""
Created on Sun May  9 09:59:11 2021

@author: ANIL
"""

'''
Python program to split and join a string

Ex:
Split the string into list of strings

Input : Geeks for Geeks
Output : ['Geeks', 'for', 'Geeks']


Join the list of strings into a string based on delimiter ('-')

Input :  ['Geeks', 'for', 'Geeks']
Output : Geeks-for-Geeks
'''


string = 'Geeks for Geeks'

words = string.split()

result = "-".join(words)

print(result)

