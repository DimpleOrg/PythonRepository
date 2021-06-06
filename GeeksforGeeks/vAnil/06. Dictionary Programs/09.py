# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:39:15 2021

@author: ANIL
"""

'''
Check order of character in string
Input: 
string = "engineers rock"
pattern = "er";
Output: true
Explanation: 
All 'e' in the input string are before all 'r'.
'''
def checkPattern(string, pattern):
    if len(string) < len(pattern):
        return False
    prev = '\0'
    for curr in pattern:
        firstIndex = string.find(curr)
        lastIndex = string.rfind(prev)
 
        if firstIndex == -1 or (prev != '\0' and lastIndex > firstIndex):
            return False
        prev = curr
    return True

input = 'engineers rock'
pattern = 'egr'
print (checkOrder(input,pattern))

if checkPattern(input, pattern):
    print("Pattern found")
else:
    print("Pattern not found")
 