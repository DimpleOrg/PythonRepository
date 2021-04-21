# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:47:29 2021

@author: ANIL
"""

'''
Python | Remove empty tuples from a list


Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]
Output : [('ram', '15', '8'), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('', '')]

Input : tuples = [('','','8'), (), ('0', '00', '000'), 
                 ('birbal', '', '45'), (''), (),  ('',''),()]
Output : [('', '', '8'), ('0', '00', '000'), ('birbal', '', 
          '45'), ('', '')]

'''


tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]


output = list(filter(None, tuples))

print(output)



output = [x for x in tuples if x]

print(output)