# -*- coding: utf-8 -*-
"""
Created on Tue May  4 07:14:02 2021

@author: dimpl
"""

# Python | Check if a Substring is Present in a Given String
# Input : s1 = geeks s2=geeks for geeks
# Output : yes

# Input : s1 = geek s2=geeks for geeks
# Output : yes


# Method 1: find()
# find() function returns -1 if it is not found, else it returns the first occurrence

sub_str = "geeks f"
string = "geeks for geeks"
if string.find(sub_str) == -1:
    print("substring not present")
else:
    print("substring present")


# Method 2: count()
if string.count(sub_str) > 0:
    print("substring present")
else:
    print("substring not present")


# Method 3: regular expression
import re

if re.search(sub_str, string):
    print("substring present")
else:
    print("substring not present")


# Method 4:
sub_str = "ks"
if sub_str in string:
    print("substring present")
else:
    print("substring not present")
