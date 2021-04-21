# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:59:34 2021

@author: dimpl
"""

# Break a list into chunks of size N in Python

# Method 1: Using yield
# The yield keyword enables a function to comeback where it left off when it is 
# called again. This is the critical difference from a regular function. A regular 
# function cannot comes back where it left off. The yield keyword helps a function 
# to remember its state. The yield enables a function to suspend and resume while 
# it turns in a value at the time of the suspension of the execution.


my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky','nerdy', 'geek', 'love',
               'questions','words', 'life']

# divide n-sized chunks from l.
def divide_chunks(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]
        
n=5
x=[]
x=list(divide_chunks(my_list, n))
print(x)
    
    
# Method 2: Using List comprehension
res=[my_list[i:i+n] for i in range(0,len(my_list),n)]
print(res)