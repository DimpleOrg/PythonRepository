# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:55:49 2021

@author: ANIL
"""
import json
try:
    with open('fav_num12.json') as f:
        fav_num = json.load(f)
except:
    fav_num = input('Enter your favorite number: ')
    with open('fav_num12.json', 'w') as f:
        json.dump(fav_num, f)
else:
    print(f'I know your favorite number! It is {fav_num}.')
