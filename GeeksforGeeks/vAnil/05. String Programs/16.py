# -*- coding: utf-8 -*-
"""
Created on Sun May  9 08:59:12 2021

@author: ANIL
"""

'''
Generating random strings until a given string is generated
'''

import string
import random

in_str = 'as$45'

chars = string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters
chars += '{}$#@'


count = 1
ranStr = "".join(random.choices(chars, k = len(in_str)))
print(ranStr)

while ranStr != in_str:
    ranStr = "".join(random.choices(chars, k = len(in_str)))
    print(ranStr)
    count += 1


print('match found after', count, 'iterations')    