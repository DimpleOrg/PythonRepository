# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:44:22 2021

@author: dimpl
"""

while True:
    character = input("Enter a character: ")
    if character == 'quit':
        break

    if len(character) > 1:
        print("Enter just 1 character.")
    else:
        print(ord(character))

    print("enter 'quit' to quit.")
