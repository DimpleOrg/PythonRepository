# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:46:19 2021

@author: ANIL
"""

'''
Python program to sort a list of tuples by second Item
'''

def Sort_Tuple(tup):
	lst = len(tup)
	for i in range(0, lst):
		
		for j in range(0, lst-i-1):
			if (tup[j][1] > tup[j + 1][1]):
				temp = tup[j]
				tup[j]= tup[j + 1]
				tup[j + 1]= temp
	return tup

tup =[('for', 24), ('is', 10), ('Geeks', 28),
	('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]
		
print(Sort_Tuple(tup))
