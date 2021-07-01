# -*- coding: utf-8 -*-
"""
Created on Tue May 25 07:15:31 2021

@author: dimpl
"""

# Replace all occurrences of a substring in a string
# Input : test_str = “geeksforgeeks”
# s1 = “geek”
# s2 = “abcd”
# Output : test_str = “abcdsforabcds”

# We use maketrans() and translate(). This is inbuild way to perform this task.
# This function maintains the table internally and performs the task of swapping.

test_str = "geeksforgeeks"
temp = str.maketrans("geek", "abcd")
test_str = test_str.translate(temp)
print(test_str)  # accdsforaccds is the right output
