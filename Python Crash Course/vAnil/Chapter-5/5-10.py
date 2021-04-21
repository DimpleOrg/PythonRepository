# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:40:34 2021

@author: ANIL
"""

current_users = ['admin', 'dimple', 'vinni', 'annu', 'neha']

new_users = ['Admin', 'raj', 'rohan', 'ANNU', 'priya']

current_users_lowercase = [value.lower() for value in current_users]

for user in new_users:
    if user.lower() in current_users_lowercase:
        print(f"{user}, You need to enter new user name.")
    else:
        print(f"{user}, The user name is available.")
