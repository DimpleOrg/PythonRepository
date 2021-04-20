# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:06:36 2021

@author: ANIL
"""
dream_vaction = {}
while True:
    print('\n\nInput "quit" if you want to quit.')
    user = input('Enter your name: ')
    if (user.lower() == 'quit'):
        break

    vac = input('Enter your dream vacation: ')
    if (vac.lower() == 'quit'):
        break
    dream_vaction[user] = vac

for user, vac in dream_vaction.items():
    print(f'{user.title()} dream vaction is {vac.title()}.')

one_place = {}
while True:
    print('\n\nInput "quit" if you want to quit.')
    user = input('Enter your name: ')
    if (user.lower() == 'quit'):
        break

    place = input('Enter your dream vacation: ')
    if (vac.lower() == 'quit'):
        break
    one_place[user] = place

for user, place in dream_vaction.items():
    print(f'{user.title()} dream vaction is {place.title()}.')
