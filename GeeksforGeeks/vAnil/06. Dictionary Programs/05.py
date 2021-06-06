# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:08:56 2021

@author: ANIL
"""

'''
Ways to sort list of dictionaries by values in Python – Using lambda function
'''

lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]
 

print("The list printed sorting by age: ")
print(sorted(lis, key = lambda i: i['age']))
 
print ("\n")
 
print("The list printed sorting by age and name: ")
print(sorted(lis, key = lambda i: (i['age'], i['name'])))
 
print ("\n")
 
print("The list printed sorting by age in descending order: ")
print(sorted(lis, key = lambda i: i['age'],reverse=True))