# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:06:44 2021

@author: ANIL
"""

'''
Break a list into chunks of size N in Python
'''

my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky','nerdy', 'geek', 'love',
               'questions','words', 'life']

n = 4

chunk_list = []

for i in range(0,(len(my_list) + n - 1)//n):
    list1 = my_list[i*n : (i+1) * n]
    chunk_list.append(list1)
    
print(chunk_list)




chunk_list1 = [ my_list[i:i+n] for i in range(0,len(my_list),n)]
print(chunk_list1)



def divide_chunks(l, n):
    for i in range(0, len(l), n): 
        yield l[i:i + n]
        
x = list(divide_chunks(my_list, n))
print (x)