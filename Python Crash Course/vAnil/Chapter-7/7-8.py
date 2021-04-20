# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 16:53:38 2021

@author: ANIL
"""

sandwich_orders = ['sadwitch_a', 'sadwitch_b', 'sadwitch_c', 'sadwitch_d']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich.title()}.')

    finished_sandwiches.append(sandwich)

while finished_sandwiches:
    print(f'{finished_sandwiches.pop().title()} is made.')
