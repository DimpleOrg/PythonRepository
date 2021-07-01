# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:45:19 2021

@author: dimpl
"""

# Find words which are greater than given length k
str = "hello geeks for geeks is computer science portal"
k = 4
res = [word for word in str.split() if len(word) > k]
print(*res)
