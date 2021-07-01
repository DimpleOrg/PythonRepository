# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:24:37 2021

@author: dimpl
"""

# Convert Snake case to Pascal case
# The original string is : geeksforgeeks_is_best
# The String after changing case : GeeksforgeeksIsBest

input_str = "geeksforgeeks_is_best"
res_str = input_str.split("_")
res_str1 = "".join([each.title() for each in res_str])
print(res_str1)


# Method 2: replace()
res_str2 = input_str.replace("_", " ").title().replace(" ", "")
print(res_str2)


# Method 3:
import string

res_str3 = string.capwords(input_str.replace("_", " ")).replace(" ", "")
print(res_str3)
