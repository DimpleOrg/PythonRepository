# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:37:01 2021

@author: ANIL
"""

usernames = []

if usernames:
    for user in usernames:
        if(user == 'admin'):
            print("Hello admin, would you like to see a status report?")
        else:
            print(f'Hello {user}, thank you for loggin in again.')
else:
    print('We need to find some users!')
