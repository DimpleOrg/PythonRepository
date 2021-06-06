# -*- coding: utf-8 -*-
"""
Created on Sun May 30 13:15:23 2021

@author: ANIL
"""

'''
String slicing in Python to check 
if a string can become empty by recursive deletion
'''
str1 = "GEEGEEKSKS"
sub_str = "GEEKS"

ans = True
while len(str1) >= len(sub_str):
    index = str1.find(sub_str) 
    if index == -1:
        ans = False
        break
    else:
        str1 = str1[:index] + str1[index+len(sub_str):]
        print(str1)
        
        
        
        
print(ans)
