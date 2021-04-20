# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:58:23 2021

@author: ANIL
"""

import json


def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
    else:
        result = input(f'Your user name is {username} (yes/no)? ')
        if result.lower() == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = input("What is your name? ")
            with open(filename, 'w') as f:
                json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")


greet_user()
