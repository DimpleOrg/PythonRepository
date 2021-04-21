# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:04:29 2021

@author: ANIL
"""


def show_toppings(*items):
    print('\nList of items on piza: ')
    for item in items:
        print(item.title())


show_toppings('cheese', 'mashroom', 'salt')
show_toppings('item1', 'item2', 'item3')
show_toppings('item4', 'item5', 'item6')
