# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:58:14 2021

@author: ANIL
"""
favorite_numbers = {
    'Jack Ma': [100, 104, 108],
    'Bill Gates': [41, 51, 61],
    'Mukesh Ambani': [33, 43, 53],
    'Azim Premji': [9, 19, 29],
    'Ratan Tata': [101, 111, 121],
}
for person in favorite_numbers:
    print(f'{person.title()}: {favorite_numbers[person]}')
