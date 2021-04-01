# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:09:12 2021

@author: dimpl
"""

# Python Program for Reversal algorithm for array rotation
# Write a function rotate(arr[], d, n) that rotates arr[] of size n by d elements.
# Example :

# Input :  arr[] = [1, 2, 3, 4, 5, 6, 7]

#          d = 2
#          n = 7
# Output : arr[] = [3, 4, 5, 6, 7, 1, 2]

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = 7


def rotate(d, n):
    arr.reverse()
    reverse_list(0, n-d-1)
    reverse_list(n-d, n-1)


def reverse_list(start, end):
    # arr.reverse()
    len = (end-start+1)//2
    for i in range(len):
        temp = arr[start]
        arr[start] = arr[end-i]
        arr[end-i] = temp
        start += 1


#rotate_split(2, 7, arr)
# rotate(2, 7)
arr = arr[d:n]+arr[:d]
print(arr)
