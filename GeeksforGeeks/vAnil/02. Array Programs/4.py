# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:38:39 2021

@author: ANIL
"""

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n =7

arr1 = arr[d+1:n]
arr2 = arr[:d]

print(arr1)
print(arr2)
arr1.reverse()
arr2.reverse()

arr = arr2 + arr1

arr.reverse()


print(arr)