# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 15:34:58 2021

@author: ANIL
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_list = ['jen', 'tom', 'mark', 'sarah', 'edward', 'phil']

for people in people_list:
    if people in favorite_languages.keys():
        print(f'Thank you {people.title()} for responding.')
    else:
        print(f'{people.title()} you are invited to take the poll.')
