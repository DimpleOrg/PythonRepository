# -*- coding: utf-8 -*-
"""
Created on Sun May 30 12:49:31 2021

@author: ANIL
"""

'''
Execute a String of Code in Python
'''


LOC = """
def factorial(num):
	fact=1
	for i in range(1,num+1):
		fact = fact*i
	return fact
print(factorial(5))
"""

exec(LOC)
	
