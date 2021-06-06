# -*- coding: utf-8 -*-
"""
Created on Sun May 16 12:25:47 2021

@author: ANIL
"""

'''
Python | Check for URL in a String
'''

import re

string = 'My Profile: \
https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles \
in the portal of http://www.geeksforgeeks.org/'


ur = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)

print(ur)