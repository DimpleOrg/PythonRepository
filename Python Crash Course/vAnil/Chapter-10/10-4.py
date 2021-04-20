# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:06:40 2021

@author: ANIL
"""

with open('guest_book.txt', 'w') as f:
    while True:
        name = input('Please input your name: (or q to quit) ')
        if name == 'q':
            break
        else:
            print(f'welcome {name}')
            name += '\n'
            f.write(name)
