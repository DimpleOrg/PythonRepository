# -*- coding: utf-8 -*-
"""
Created on Tue May  4 04:27:37 2021

@author: ANIL
"""

'''
Reverse words in a given String in Python
'''


s = 'hello world how are you'

words = s.split()

answer = " ".join(reversed(words))

print(answer)

