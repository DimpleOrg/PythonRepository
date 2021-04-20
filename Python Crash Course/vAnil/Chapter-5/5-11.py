# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:47:22 2021

@author: ANIL
"""
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')
