# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:54:41 2021

@author: dimpl
"""

# Given a dictionary and a character array, print all valid words that are possible
# using characters from the array.
# Note: Repetitions of characters is not allowed.
# Examples:

# Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
#         arr = ['e','o','b', 'a','m','g', 'l']
# Output : go, me, goal.

from math import factorial


Dict = ["go", "bat", "me", "eat", "goal", "boy", "run"]
arr = ["e", "o", "b", "a", "m", "g", "l"]


if factorial(len(arr)) > len(Dict):
    arr_string = "".join(arr)
    for each in Dict:
        if each in arr_string:
            print(each)
