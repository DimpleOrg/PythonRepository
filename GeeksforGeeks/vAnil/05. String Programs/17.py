# -*- coding: utf-8 -*-
"""
Created on Sun May  9 09:54:13 2021

@author: ANIL
"""

'''
Find words which are greater than given length k

Input : str = "hello geeks for geeks 
          is computer science portal" 
        k = 4
Output : hello geeks geeks computer 
         science portal
'''

k = 3
test_str ="geek for geeks"

result = [x for x in test_str.split() if(len(x)>k)]

print(*result)
