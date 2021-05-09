# -*- coding: utf-8 -*-
"""
Created on Sun May  9 09:48:20 2021

@author: ANIL
"""

'''
Program to check if a string contains any special character
'''

special_chars = set("[@_!#$%^&*()<>?/|}{~:]")

test_string =  "Geeks$For$Geeks"

intersection = special_chars.intersection(test_string)

if len(intersection) > 0:
    print('String contains special charters:', intersection)
else:
    print('No special char found')