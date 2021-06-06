# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:06:16 2021

@author: ANIL
"""

'''
Ways to sort list of dictionaries by values in Python – Using itemgetter
'''

from operator import itemgetter

lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

print(sorted(lis, key=itemgetter('age')))

print ("\n")

print("The list printed sorting by age and name: ")
print(sorted(lis, key=itemgetter('age', 'name')))

print ("\n")

print("The list printed sorting by age in descending order: ")
print(sorted(lis, key=itemgetter('age'),reverse = True))
