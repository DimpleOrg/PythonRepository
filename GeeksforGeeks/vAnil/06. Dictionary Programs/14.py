# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 16:57:30 2021

@author: ANIL
"""

'''
Handling missing keys in Python dictionaries

'''


#method-1
country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

# search dictionary for country code of India
print(country_code.get('India', 'Not Found'))

# search dictionary for country code of Japan
print(country_code.get('Japan', 'Not Found'))


#method-2
country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

# Set a default value for Japan
country_code.setdefault('Japan', 'Not Present')

# search dictionary for country code of India
print(country_code['India'])

# search dictionary for country code of Japan
print(country_code['Japan'])
