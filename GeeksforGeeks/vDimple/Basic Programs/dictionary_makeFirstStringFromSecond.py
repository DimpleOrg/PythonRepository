# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:50:24 2021

@author: dimpl
"""

# Given two strings, find if we can make first string from second by deleting some characters from second and rearranging remaining characters.

# Input : s1 = ABHISHEKsinGH
#       : s2 = gfhfBHkooIHnfndSHEKsiAnG
# Output : Possible

from collections import Counter

s1 = "ABHISHEKsinGH"
s2 = "gfhfHkoBoIHnfndSHEKsiAnG"

dict1 = Counter(s1)
dict2 = Counter(s2)

res = dict1 & dict2

if res == dict1:
    res = True
else:
    res = False

print(res)
