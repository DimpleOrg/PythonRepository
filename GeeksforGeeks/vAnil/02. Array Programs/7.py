# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:10:35 2021

@author: ANIL
"""

'''
Given an array A containing n integers. The task is to check whether the array is Monotonic or not. An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return “True” if the given array A is monotonic else return “False” (without quotes).

Examples:

Input : 6 5 4 4
Output : true

Input : 5 15 20 10
Output : false
'''

A = [6, 5, 4, 4]
n = len(A)

result = False

for i in range(0,n-1):
    if A[i] <= A[i+1]:
        result = True
    else:
        result = False
        break
    
    
if result == False:
    for i in range(0,n-1):
        if A[i] >= A[i+1]:
            result = True
        else:
            result = False
            break
    
print(result)
    

    