# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:39:46 2021

@author: ANIL
"""

'''
Given a string, the task is to check if every vowel is present or not. We consider a vowel to be present if it is present in upper case or lower case. i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ . 
Input : geeksforgeeks
Output : Not Accepted
'''

string = 'geeksforgeeks'

set1 = set(string.lower())

set2 = set1 & set('aeiou')

if len(set2) == 5:
    print('Accepted')
else:
    print('Not Accepted')
