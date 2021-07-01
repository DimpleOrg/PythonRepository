# -*- coding: utf-8 -*-
"""
Created on Fri May 14 07:34:41 2021

@author: dimpl
"""

# Replace multiple words with K
test_str = "Geeksforgeeks is best for geeks and CS"

# initializing word list
word_list = ["best", "CS", "for"]

# initializing replace word
repl_wrd = "replaced"

res = " ".join([repl_wrd if word in word_list else word for word in test_str.split()])

print(res)
