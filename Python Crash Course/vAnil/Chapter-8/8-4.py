# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:23:27 2021

@author: ANIL
"""


def make_shirt(size='L', text='I love Python'):
    print(f'SIZE:{size} MESSAGE:{text}')


make_shirt(size='L', text='Hello World!')
make_shirt(text='Hello Python!', size='M')
make_shirt()
make_shirt(text='Hello Python!', size='M')
make_shirt()
make_shirt('M')
