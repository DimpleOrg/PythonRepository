# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:45:51 2021

@author: dimpl
"""

# String slicing in Python to check if a string can become empty by recursive deletion
# Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
# Output : Yes

# =============================================================================
# Use find() method of string to search given pattern sub-string.
# If sub-string lies in main string then find function will return index of it’s
#  first occurrence.
# Now slice string in two parts, (i) from start of string till index-1 of founded
# sub-string, (ii) (start from first index of founded sub-string + length of
# sub-string) till end of string.
# Concatenate these two sliced part and repeat from step 1 until original string
# becomes empty or we don’t find sub-string anymore.
# =============================================================================

str = "GEEGEEKSKS"
sub_str = "GEEK"
if len(str) == 0 or len(sub_str) == 0:
    print("true")
else:
    flag = True
    while len(str) > 0:
        index = str.find(sub_str)
        if index != -1:
            res = str[:index] + str[index + len(sub_str) :]
            str = res
        else:
            flag = False
            break
    print(flag)
