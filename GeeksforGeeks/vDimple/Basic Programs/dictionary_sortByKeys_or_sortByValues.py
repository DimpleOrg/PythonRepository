# -*- coding: utf-8 -*-
"""
Created on Sun May 30 22:27:25 2021

@author: dimpl
"""

# Sort Python Dictionaries by Key or Value

# Problem Statement – Here are the major tasks that are needed to be performed.

# Create a dictionary and display its keys alphabetically.
# Display both the keys and values sorted in alphabetical order by the key.
# Same as above part, but sorted in alphabetical order by the value.


# Sort the dictionary by key
# Note:it will sort in lexicogrphical order
# Taking key’s type as string
from collections import OrderedDict

dict = {"ravi": "10", "rajnish": "9", "sanjeev": "15", "yash": "2", "suraj": "32"}
res = OrderedDict(sorted(dict.items()))
print(*res)


# Displaying the Keys Alphabetically:
# Examples:

# Input:
# key_value[2] = '64'
# key_value[1] = '69'
# key_value[4] = '23'
# key_value[5] = '65'
# key_value[6] = '34'
# key_value[3] = '76'

# Output:
# 1 2 3 4 5 6


# Sorting the Keys and Values in Alphabetical Order using the Key.
# Examples:

# Input:
# key_value[2] = '64'
# key_value[1] = '69'
# key_value[4] = '23'
# key_value[5] = '65'
# key_value[6] = '34'
# key_value[3] = '76'

# Output:
# (1, 69) (2, 64) (3, 76) (4, 23) (5, 65) (6, 34)


# Sorting the Keys and Values in alphabetical using the value
# Examples:

# Input:
# key_value[2] = '64'
# key_value[1] = '69'
# key_value[4] = '23'
# key_value[5] = '65'
# key_value[6] = '34'
# key_value[3] = '76'

# Output:
# (4, 23), (6, 34), (2, 64), (5, 65), (1, 69), (3, 76)
