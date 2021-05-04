# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 08:40:49 2021

@author: dimpl
"""

# Python program to check if a string is palindrome or not
# Input : malayalam
# Output : Yes

# Input : geeks
# Output : No


# Method 1: Iterative Method
str = "malaalam"
length_str = len(str)
flag = True

for i in range(length_str // 2):
    if str[i] != str[-1 - i]:
        flag = False
        break

if flag:
    print(f"String {str} is palindrome.")
else:
    print(f"String {str} is not palindrome.")


# Method 2: Method using the inbuilt function to reverse a string.
str = "malayalam"
rev_str = "".join(reversed(str))
if str == rev_str:
    print(f"String {str} is palindrome.")
else:
    print(f"String {str} is not palindrome.")
