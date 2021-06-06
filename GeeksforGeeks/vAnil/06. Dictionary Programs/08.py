# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:24:05 2021

@author: ANIL
"""

'''
Insertion at the beginning in OrderedDict
Input: 
original_dict = {'a':1, 'b':2}
item to be inserted ('c', 3)

Output:  {'c':3, 'a':1, 'b':2}

Input: 
original_dict = {'akshat':1, 'manjeet':2}
item to be inserted ('nikhil', 3)

Output:  {'nikhil':3, 'akshat':1, 'manjeet':2}
'''

from collections import OrderedDict

iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])
print(iniordered_dict)

iniordered_dict.update({'manjeet':'3'})
iniordered_dict.move_to_end('manjeet', last = False)

print ("Resultant Dictionary : "+str(iniordered_dict))
