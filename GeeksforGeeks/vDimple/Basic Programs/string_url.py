# -*- coding: utf-8 -*-
"""
Created on Fri May 14 07:57:39 2021

@author: dimpl
"""

# Check for URL in a String
# Input : string = 'My Profile:
# https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles
# in the portal of http://www.geeksforgeeks.org/'

# Output : URLs :  ['https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles',
# 'http://www.geeksforgeeks.org/']

# To find the URLs in a given string we have used the findall() function from the
# regular expression module of Python. This return all non-overlapping matches of
# pattern in string, as a list of strings. The string is scanned left-to-right, and
# matches are returned in the order found.

string = "My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles \
in the portal of http://www.geeksforgeeks.org/"

import re

my_str = "Hi my name is John and email john+123john@gmail.abc address is john.doe@somecompany.co.uk and my friend's email is jane_doe124@gmail.com john123@gmail.com"
emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)", my_str)

for mail in emails:
    print(mail)
