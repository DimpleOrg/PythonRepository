# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:52:35 2021

@author: ANIL
"""
import json
try:
    with open('fav_num.json') as f:
        fav_num = json.load(f)
except:
    pass
else:
    print(f'I know your favorite number! It is {fav_num}.')
