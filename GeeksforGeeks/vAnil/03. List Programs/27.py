# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:06:35 2021

@author: ANIL
"""

'''
The problem statement asks to produce a new list whose i^{th} element will be equal to the sum of the (i + 1) elements.

Examples : 
 

Input : list = [10, 20, 30, 40, 50]
Output : [10, 30, 60, 100, 150]

Input : list = [4, 10, 15, 18, 20]
Output : [4, 14, 29, 47, 67]
'''

list1 = [10, 20, 30, 40, 50]

sumList = [list1[0]]


for item in range(1,len(list1)):
    temp = sumList[-1] + list1[item] 
    sumList.append(temp)
    
print(sumList)