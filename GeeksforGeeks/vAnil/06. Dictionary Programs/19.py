# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:44:34 2021

@author: ANIL
"""

'''
Python Counter to find the size of largest subset of anagram words
'''

arr = 'ant magenta magnate tan gnamate'

arr = arr.split()

dic = {}

for item in arr:
    sitem = "".join(sorted(item));
    
    if sitem in dic.keys():
        dic[sitem].append(item)
    else:
        dic[sitem] = [item]
    
largest = 0
for key in dic.keys():
    if len(dic[key]) > largest:
        largest = len(dic[key])
        
print(largest)