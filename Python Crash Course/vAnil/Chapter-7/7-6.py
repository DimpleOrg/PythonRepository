# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 16:49:22 2021

@author: ANIL
"""
active = True
while active:
    msg = input('Enter a series of pizza toppings or type "quit": ')
    if msg == 'quit':
        active = False
    else:
        print(f'I will add {msg.title()} topping to your pizza.')


while True:
    msg = input('Enter a series of pizza toppings or type "quit": ')
    if msg == 'quit':
        break
    else:
        print(f'I will add {msg.title()} topping to your pizza.')
