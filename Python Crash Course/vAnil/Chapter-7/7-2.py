# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:34:17 2021

@author: ANIL
"""
no_people = input('How many people are in their dinner group? ')
no_people = int(no_people)
if no_people > 8:
    print("They'll have to wait for table.")
else:
    print('Their table is ready.')
