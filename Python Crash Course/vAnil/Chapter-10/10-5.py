# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:11:36 2021

@author: ANIL
"""

with open('poll_reason.txt', 'w') as f:
    while True:
        name = input('Why they like programming: (or q to quit) ')
        if name == 'q':
            break
        else:
            name += '\n'
            f.write(name)
