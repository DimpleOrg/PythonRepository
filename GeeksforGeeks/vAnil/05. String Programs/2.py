# -*- coding: utf-8 -*-
"""
Created on Tue May  4 04:12:44 2021

@author: ANIL
"""

'''
Python program to check whether the string is Symmetrical or Palindrome
'''

def checkPalindrome(s):
    if s == s[::-1]:
        print('Palindrome')
    else:
        print('Not Palindrome')   


def checkSymmetrical(s):
    mid = len(s)//2

    i = 0
    while i < mid:
        if s[i] != s[mid+i]:
            print('Not Symmetrical')
            return
        i += 1

    print('Symmetrical')        


s = 'abcba'
s1 = 'adpadp'

checkPalindrome(s)
checkSymmetrical(s1)
    
    
