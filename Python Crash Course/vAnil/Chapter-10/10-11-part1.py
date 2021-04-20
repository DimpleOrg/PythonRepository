# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:49:41 2021

@author: ANIL
"""
import json

fav_num = input('Enter your favorite number: ')
with open('fav_num.json', 'w') as f:
    json.dump(fav_num, f)
