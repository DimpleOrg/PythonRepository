# -*- coding: utf-8 -*-
"""
Created on Sat May  8 07:00:12 2021

@author: dimpl
"""

# Program to check if a string contains any special character
import re

str1 = "geeks@for$ geeks"

# Make own character set and pass
# this as argument in compile method
regex = re.compile("[@_!#$%^&*()<>?/\|}{~:]")

if re.search(regex, str1) == None:
    print("string has no special characters")
else:
    print("String has special characters.")


# Method 2:
spcl_char = "[@_!#$%^&*()<>?/\|}{~:]"
res = set(str1) & set(spcl_char)
if res == None:
    print("string has no special characters")
else:
    print("String has ", res, "special characters.")
