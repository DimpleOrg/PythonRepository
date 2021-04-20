# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:29:40 2021

@author: ANIL
"""


def city_country(city, country):
    msg = f'"{city.title()}","{country.title()}"'
    return msg


val = city_country('lucknow', 'india')
print(val)

val = city_country('bhopal', 'india')
print(val)
