# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:54:04 2021

@author: dimpl
"""

# Check if a given string is binary string or not
str1 = "01010101010"
str2 = "geeks101"
str3 = "00000000000"
str4 = "111111"
str5 = "01"
binary = {"0", "1"}
if set(str1) == set("01") or set(str1) == set("0") or set(str1) == set("1"):
    print("It's Binary")
else:
    print("It's Not Binary")
