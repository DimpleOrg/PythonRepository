# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:18:57 2021

@author: ANIL
"""

'''
Python – Convert Snake case to Pascal case
Input : geeks_for_geeks
Output : GeeksforGeeks
'''

test_str = 'geeksforgeeks_is_best'

words = [ word.title() for word in test_str.split('_')]

result_str = ''

for word in words:
    result_str += word

print(result_str)



#method2
test_str = 'geeksforgeeks_is_best'
result_str = test_str.replace("_", " ").title().replace(" ", "")
print(result_str)