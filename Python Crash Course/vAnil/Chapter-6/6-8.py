# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:28:37 2021

@author: ANIL
"""
doggy = {
    'type': 'dog',
    'owner': 'sam pitroda',
}

catty = {
    'type': 'cat',
    'owner': 'preeti rai',
}

milky = {
    'type': 'cow',
    'owner': 'ramesh chandra',
}

pets = [doggy, catty, milky]
for pet in pets:
    print(f"Type:\t\t{pet['type'].title()}")
    print(f"Owner:\t\t{pet['owner'].title()}\n")
