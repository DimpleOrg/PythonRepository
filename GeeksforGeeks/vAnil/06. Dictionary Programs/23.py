# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:28:09 2021

@author: ANIL
"""
'''
Convert a list of Tuples into Dictionary
'''


tups = [("akash", 10), ("gaurav", 12), ("anand", 14), 
     ("suraj", 20), ("akhil", 25), ("ashish", 30)]


dic = {}

for item in tups:
    dic.setdefault(item[0],[]).append(item[1])
    
print(dic)