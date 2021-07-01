# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:31:12 2021

@author: dimpl
"""

# Generating random strings until a given string is generated
import random
import string

possible_chars = string.ascii_letters + string.digits + " .,!?;:"
given_str = "off"
res = ""
while res != given_str:
    res = "".join(random.choice(possible_chars) for i in range(len(given_str)))
    print(res)
