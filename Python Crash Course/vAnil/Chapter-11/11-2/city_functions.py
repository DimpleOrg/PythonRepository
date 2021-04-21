# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:07:10 2021

@author: ANIL
"""


# def fun(city, country, population):
#     return f'{city}, {country}, "-" {population}'


def fun(city, country, population=None):
    if population:
        return f'{city}, {country} - population {population}'
    else:
        return f'{city}, {country}'
