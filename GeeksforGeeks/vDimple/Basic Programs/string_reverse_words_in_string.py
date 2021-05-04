# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 09:14:28 2021

@author: dimpl
"""

# Reverse words in a given String in Python.
# Input : str = geeks quiz practice code
# Output : str = code practice quiz geeks

str = "geeks quiz practice code"
words = str.split(" ")
res_str = " ".join(reversed(words))
print(res_str)
