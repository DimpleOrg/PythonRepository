# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:39:37 2021

@author: ANIL
"""

'''
Check if element exists in list in Python
'''

test_list = [ 1, 6, 3, 5, 3, 4 ]
check_elem = 4


if check_elem in test_list:
    print(f'Element {check_elem} is found in the list.')
else:
    print(f'Element {check_elem} is NOT found in the list.')