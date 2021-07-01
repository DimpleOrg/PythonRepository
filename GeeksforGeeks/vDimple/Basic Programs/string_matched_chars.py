# -*- coding: utf-8 -*-
"""
Created on Fri May  7 07:26:13 2021

@author: dimpl
"""

# Count the Number of matching characters in a pair of string
str1 = "abcdef"
str2 = "defghia"
ctr = 0
for i in str1:
    if i in str2:
        ctr += 1
print(ctr)


# Method 2:
matched_chars = set(str1) & set(str2)
print(len(matched_chars))


# Method 3:
print(len(set(str1).intersection(set(str2))))
