# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:04:15 2021

@author: ANIL
"""

name = input("Please give your name: ")
with open('guest.txt', 'w') as f:
    f.write(name)
