# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 16:22:05 2021

@author: ANIL
"""


def make_album(name, title):
    info = {name: title}
    return info


while True:
    print('\n\nEnter "quit" to exit.')
    name = input('Enter the artist name: ')
    if name == 'quit':
        break

    album = input('Enter the album title: ')
    if album == 'quit':
        break

    print(make_album(name, album))
