# -*- coding: utf-8 -*-
"""
Created on Fri May  7 08:56:47 2021

@author: dimpl
"""

# Most Frequent Character in String
from collections import Counter

str1 = "geeksforgeeks is best."
res = Counter(str1)
res = max(res, key=res.get)
print(res)


# Method 2:
all_freq = {}
for i in str1:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# We find minimum occurring character by using min() on values.
res1 = max(all_freq, key=all_freq.get)
print(res1)
