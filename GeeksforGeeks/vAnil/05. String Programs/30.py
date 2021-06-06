# -*- coding: utf-8 -*-
"""
Created on Sun May 30 13:40:34 2021

@author: ANIL
"""

'''
Sometimes, while working with Python strings, we can have a problem in which we need to replace all occurrences of a substring with other.

Input : test_str = “geeksforgeeks”
s1 = “geeks”
s2 = “abcd”
Output : test_str = “abcdsforabcds”
Explanation : We replace all occurrences of s1 with s2 in test_str.

Input : test_str = “geeksforgeeks”
s1 = “for”
s2 = “abcd”
Output : test_str = “geeksabcdgeeks”
'''

test_str = "geeksforgeeks"
  
print("The original string is : " + test_str)

temp = str.maketrans("geek", "abcd")
test_str = test_str.translate(temp)
  
print("The string after swap : " + str(test_str)) 