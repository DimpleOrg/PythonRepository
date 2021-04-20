# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 15:44:13 2021

@author: ANIL
"""
person1 = {
    'first_name': 'Jack',
    'last_name': 'Ma',
    'age': 56,
    'city': 'Hangzhou',
}
person2 = {
    'first_name': 'Tom',
    'last_name': 'jerry',
    'age': 6,
    'city': 'kabul',
}
person3 = {
    'first_name': 'bill',
    'last_name': 'ton',
    'age': 88,
    'city': 'newyork',
}

persons = [person1, person2, person3]
for person in persons:
    print(
        f"Name:\t{person['first_name'].title()} {person['last_name'].title()}")
    print(f"Age:\t{person['age']}")
    print(f"City:\t{person['city'].title()}")
    print('\n')
