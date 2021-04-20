# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 16:42:20 2021

@author: ANIL
"""
flag = True
while flag:
    age = input('Please enter your age: ')
    age = int(age)

    if age < 3:
        print('Ticket is free.')
    elif (age > 3) and (age <= 12):
        print('The ticket is $10')
    else:
        print('The ticket is $15')
