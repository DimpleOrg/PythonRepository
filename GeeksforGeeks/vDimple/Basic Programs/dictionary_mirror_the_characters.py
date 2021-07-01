# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:26:10 2021

@author: dimpl
"""

# Given a string and a number N, we need to mirror the characters from the N-th position
# up to the length of the string in alphabetical order. In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.
# Examples:


# Input : N = 3
#         paradox
# Output : paizwlc

original = "abcdefghijklmnopqrstuvwxyz"
reverse = "zyxwvutsrqponmlkjihgfedcba"

string = "paradox"
n = 3

newString = string[: n - 1]
for i in range(n - 1, len(string)):
    pos = original.find(string[i])
    newString += reverse[pos]

print(newString)


# ***************Method 2:Zip

list_tuple = list(zip(original, reverse))
newString1 = string[0 : n - 1]
for i in range(n - 1, len(string)):
    newString1 += list_tuple[ord(string[i]) - ord("a")][1]
print(newString1)
