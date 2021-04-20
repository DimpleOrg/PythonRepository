# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 17:04:37 2021

@author: ANIL
"""
cities = {
    'delhi': {
        'country': 'India',
        'population': '2 crores',
        'fact': 'capital of India'
    },
    'lucknow': {
        'country': 'India',
        'population': '50 lakhs',
        'fact': 'capital of UP',
    },
    'mumbai': {
        'country': 'India',
        'population': '1 crore',
        'fact': 'city of Indian film industry.'
    },
}
for city in cities:
    print(f'\nCity:\t\t\t{city.title()} \nInformations:')
    for key, value in cities[city].items():
        print(f'\t\t\t\t{key.title()}:\t{value}')

print('\n')
