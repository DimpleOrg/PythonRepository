# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:08:04 2021

@author: ANIL
"""

from random import choice

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

my_ticet = [10, 'd']

won = []
for i in range(4):
    won.append(choice(data))

print(won)

count = 1
while True:
    #won = choice(data)
    if won in my_ticet:
        print('You win.')
        break
    else:
        count += 1

print(f'Loop run {count} times to win.')
