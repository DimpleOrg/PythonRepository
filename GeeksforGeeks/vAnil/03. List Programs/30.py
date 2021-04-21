# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:06:49 2021

@author: ANIL
"""

'''
Given two lists, sort the values of one list using the second list.
 

Examples: 

Input : list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

Output :['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']
'''

def sort_list(list1, list2):
 
    zipped_pairs = zip(list2, list1)
 
    z = [x for _, x in sorted(zipped_pairs)]
     
    return z


x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

print(sort_list(x, y))

x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
 
print(sort_list(x, y))