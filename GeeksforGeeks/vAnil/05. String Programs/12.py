# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:47:14 2021

@author: ANIL
"""

'''
We are given a string and we need to remove all duplicates from it?
What will be the output if the order of character matters?
Examples:

Input : geeksforgeeks
Output : efgkos
'''

test = 'geeksforgeeks'

result = ''

for ch in test:
    if ch in result:
        pass
    else:
        result += ch
            
        
print('With Order:',result)

print('Without Order Maintained:', "".join(set(test)))