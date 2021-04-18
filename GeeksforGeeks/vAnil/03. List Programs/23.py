# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:43:27 2021

@author: ANIL
"""
'''
Cloning or Copying a list
'''

src = [4, 8, 2, 10, 15, 18]

dst = src[:]

print(dst)


dst = [x for x in src]

print(dst)