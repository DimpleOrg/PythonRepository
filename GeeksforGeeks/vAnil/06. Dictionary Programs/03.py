# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:02:35 2021

@author: ANIL
"""

'''
Ways to remove a key from dictionary

'''

test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}

#method 1
del test_dict['Mani']
print(test_dict)


test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}

#method 2
test_dict = {key:val for key,val in test_dict.items() if key != 'Mani'}
print(test_dict)