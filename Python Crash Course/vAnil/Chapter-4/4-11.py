# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 20:12:29 2021

@author: ANIL
"""
pizzas = ['Margherita', 'Farm House', 'Peppy Paneer']
friend_pizzas = pizzas[:]

pizzas.append('Mexican Green Wave')
friend_pizzas.append('Veg Extravaganza')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
