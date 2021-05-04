# -*- coding: utf-8 -*-
"""
Created on Mon May  3 21:43:48 2021

@author: dimpl
"""

# Ways to remove i’th character from string in Python

# Method 1: Brute Force
str = "geeks for geeks"
i = 2
new_str = ""
for j in range(len(str)):
    if j != i:
        new_str += str[j]
print(new_str)


# Method 2: str.replace()
str = "geeks for geeks"
res_str = str.replace("s", "")
res_str1 = str.replace("s", "", 1)
print(res_str)
print(res_str1)


# Method 3: slice
str = "geeks for geeks"
i = 2
res = str[:i] + str[i + 1 :]
print(res)


# Method 4: str.join()
str = "geeks for geeks"
i = 2
res1 = "".join([str[j] for j in range(len(str)) if j != i])
print(res1)
