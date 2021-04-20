# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:44:46 2021

@author: ANIL
"""
glossary = {
    'print': 'to print on console',
    'for': 'to loop in list',
    'range': 'to create the number in range',
    'if': 'to check for condition',
    'elif': 'to check for conditional statments',
    'else': 'else of the condition',
    '{}':   'used for dictonary',
    '[]': 'used for list',
    '(,)': 'used for read-only list',
}

for key, value in glossary.items():
    print(f'{key}:\n\t\t{value}')
