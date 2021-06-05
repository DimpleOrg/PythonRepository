# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:34:19 2021

@author: ANIL
"""

'''
Python Dictionary | Check if binary representations of two numbers are anagram

Given two numbers you are required to check whether they are anagrams of each 
other or not in binary representation.

'''

def NumOfOnes(x):
    if x==0: return 0
    
    num = 1
    while x>1:
        if x%2:
            num += 1
        
        x = (x)//2
        
    return num

a = 15
b = 25

setBitsA = NumOfOnes(a)
setBitsB = NumOfOnes(b)

if setBitsB == setBitsA:
    print('Yes')
else:
    print('No')

 