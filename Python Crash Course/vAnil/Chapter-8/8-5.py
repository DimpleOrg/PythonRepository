# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:25:30 2021

@author: ANIL
"""


def describe_city(city, country='India'):
    print(f'{city.title()} is in {country.title()}.')


describe_city('delhi')
describe_city('gurgaon')
describe_city('lucknow')
describe_city('newyork', 'USA')
