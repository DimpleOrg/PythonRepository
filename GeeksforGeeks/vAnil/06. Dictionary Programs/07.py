# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:21:13 2021

@author: ANIL
"""

'''
Convert key-values list to flat dictionary
'''
test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
print("The original dictionary is : " + str(test_dict))
  
# Using dict() + zip()
res = dict(zip(test_dict['month'], test_dict['name']))
print("Flattened dictionary : " + str(res)) 