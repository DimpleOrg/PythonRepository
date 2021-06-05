# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:15:48 2021

@author: ANIL
"""

'''
Print anagrams together in Python using List and Dictionary
'''

arr = ['cat', 'dog', 'tac', 'god', 'act']

dic = {}

for item in arr:
    sitem = "".join(sorted(item));
    
    if sitem in dic.keys():
        dic[sitem].append(item)
    else:
        dic[sitem] = [item]
    

for key in dic.keys():
    print(*dic[key],end=" ")