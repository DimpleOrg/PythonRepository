# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:24:26 2021

@author: ANIL
"""

'''
Counting the frequencies in a list using dictionary in Python
'''

from collections import  Counter 

my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 24, 24, 2, 2]

dic = Counter(my_list)

print(dic)