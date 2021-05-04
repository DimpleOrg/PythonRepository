# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 08:58:47 2021

@author: dimpl
"""

# Python program to check whether the string is Symmetrical or Palindrome.
# A string is said to be symmetrical if both the halves of the string are the same.

# Input: khokho
# Output:
# The entered string is symmetrical
# The entered string is not palindrome

# Input:amaama
# Output:
# The entered string is symmetrical
# The entered string is palindrome

str = "khokho"
rev_str = "".join(reversed(str))
mid = len(str) // 2

if str == rev_str:
    print(f"String {str} is palindrome.")
else:
    print(f"String {str} is not palindrome.")

if str[0:mid] == str[mid:]:
    print(f"String {str} is symmetrical.")
else:
    print(f"String {str} is not symmetrical.")
