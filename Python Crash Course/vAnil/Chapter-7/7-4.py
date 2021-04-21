# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:56:42 2021

@author: ANIL
"""
flag = True
while flag:
    msg = input('Enter a series of pizza toppings or type "quit": ')
    if msg == 'quit':
        flag = False
    else:
        print(f'I will add {msg.title()} topping to your pizza.')
