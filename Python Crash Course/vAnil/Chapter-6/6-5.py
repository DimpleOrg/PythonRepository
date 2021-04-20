# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 15:28:16 2021

@author: ANIL
"""
rivers = {
    'nile': 'egypt',
    'ganga': 'India',
    'huaihe': 'China',
}
for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())
