# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:02:42 2021

@author: ANIL
"""

sandwich_orders = ['pastrami', 'sadwitch_a', 'pastrami',
                   'sadwitch_b', 'sadwitch_c', 'sadwitch_d', 'pastrami']
finished_sandwiches = []

print('Deli has run out of pastrami.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich.title()}.')

    finished_sandwiches.append(sandwich)

while finished_sandwiches:
    print(f'{finished_sandwiches.pop().title()} is made.')
