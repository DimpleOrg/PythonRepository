# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:25:47 2021

@author: dimpl
"""

# String slicing in Python to rotate a string
# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe"
#          Right Rotation : "ksGeeksforGee"

s = "GeeksforGeeks"
d = 2

left_rotation_res = s[d:] + s[0:d]
print(left_rotation_res)

right_rotation_res = s[len(s) - d :] + s[: len(s) - d]
print(right_rotation_res)
