# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:04:02 2021

@author: ANIL
"""

'''
Python – Replace multiple words with K
'''

test_str = 'Geeksforgeeks is best for geeks and CS'

# initializing word list 
word_list = ["best", 'CS', 'for']
  
# initializing replace word 
repl_wrd = 'gfg'

result = ' '.join([word if word not in word_list else repl_wrd  for word in test_str.split()])

print(result)