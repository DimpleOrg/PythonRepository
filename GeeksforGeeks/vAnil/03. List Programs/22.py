# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:41:48 2021

@author: ANIL
"""

'''
Remove empty List from List

'''

test_list = [5, 6, [], 3, [], [], 9]


new_list = [x for x in test_list if x]

print(*new_list)



test_list = [5, 6, [], 3, [], [], 9]

new_list = list(filter(None, test_list))

print(*new_list)