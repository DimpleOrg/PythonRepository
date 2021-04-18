# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 07:46:44 2021

@author: dimpl
"""

# Python | Remove empty tuples from a list

tuples_1 = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]

tuples_2 = [('','','8'), (), ('0', '00', '000'), 
                 ('birbal', '', '45'), (''), (),  ('',''),()]

# Method 1: Using the concept of List Comprehension
tuples_1_res=[x for x in tuples_1 if x]


# Method 2: Using the filter() method
# This method works in both Python 2 and Python 3 and above, but the desired 
# output is only shown in Python 2 because Python 3 returns a generator.
tuples_2_res=list(filter(None,tuples_2))


print(tuples_1_res)
print(tuples_2_res) 