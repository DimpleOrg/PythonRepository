# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:45:35 2021

@author: ANIL
"""

'''
Python – Remove Tuples of Length K
'''

test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
  
# printing original list
print("The original list : " + str(test_list))
  
# initializing K 
K = 1
  

res = [ele for ele in test_list if len(ele) != K]
  
# printing result 
print("Filtered list : " + str(res))