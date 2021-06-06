# -*- coding: utf-8 -*-
"""
Created on Sun May 16 09:03:19 2021

@author: ANIL
"""

'''
Python program to find uncommon words from two Strings
'''

A = "Geeks for Geeks" 
B = "Learning from Geeks for Geeks"

wordsA = A.split()
wordsB = B.split()


#Method1 using two for loops
result = []

for itemA in wordsA:
    if itemA not in wordsB:
        result.append(itemA)
                
for itemB in wordsB:
    if itemB not in wordsA:
        result.append(itemB)
        
print(*result)


#method2 using set
setA = set(wordsA)
setB = set(wordsB)

resultSet = setA.symmetric_difference(setB)
print(*resultSet)