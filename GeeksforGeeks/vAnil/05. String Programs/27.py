# -*- coding: utf-8 -*-
"""
Created on Sun May 30 12:51:55 2021

@author: ANIL
"""

'''
String slicing in Python to rotate a string
Input : s = "GeeksforGeeks"
        d = 2
Output : Left Rotation  : "eksforGeeksGe" 
         Right Rotation : "ksGeeksforGee"  


Input : s = "qwertyu" 
        d = 2
Output : Left rotation : "ertyuqw"
         Right rotation : "yuqwert"
'''

s = "GeeksforGeeks"
d = 2

#left rotation
s = s[d:]+s[:d]
print('left:', s)

s = "qwertyu" 
#right rotation
l = len(s)
s = s[-d:] + s[:-d]
print(s)