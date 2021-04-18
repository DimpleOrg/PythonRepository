# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:31:48 2021

@author: ANIL
"""
'''
Remove multiple elements from a list in Python
'''

'''
Input: [12, 15, 3, 10]
Output: Remove = [12, 3], New_List = [15, 10]
'''

input_list = [12, 15, 3, 10]

remove_list = [12,3]

modified_list = [x for x in input_list if x not in remove_list]

print(*modified_list)


'''
Input: [11, 5, 17, 18, 23, 50]
Output: Remove = [1:5], New_list = [11, 50]
'''

xlist = [11, 5, 17, 18, 23, 50]
#yRem = [1:5]

del xlist[1:5]

print(*xlist)


