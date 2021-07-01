# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:37:49 2021

@author: dimpl
"""

# Given a sentence containing n words/strings. Remove all duplicates words/strings which are similar to each others.
# Examples:


# Input : Geeks for Geeks
# Output : Geeks for

# Input : Python is great and Java is also great
# Output : is also Java Python and great

st = "Geeks for Geeks"
st = st.split()
print(set(st))
