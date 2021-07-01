# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:23:21 2021

@author: dimpl
"""

# Given a string which contains lower alphabetic characters, we need to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string.

# Examples:

# Input  : str = “xyyz”
# Output : Yes
# We can remove character ’y’ from above
# string to make the frequency of each
# character same.

# Input : str = “xyyzz”
# Output : Yes
# We can remove character ‘x’ from above
# string to make the frequency of each
# character same.

# Input : str = “xxxxyyzz”
# Output : No
from collections import Counter

str1 = "xyyzz"
dicta = Counter(str1)

list_a = sorted(list(dicta.values()))

ctr = 0
flag = True
for i in range(len(list_a) - 1):
    diff = list_a[i + 1] - list_a[i]
    if diff > 1:
        flag = False
        break
    if diff == 1:
        ctr += 1

if flag == False or ctr > 1:
    print("No")
else:
    print("Yes")
