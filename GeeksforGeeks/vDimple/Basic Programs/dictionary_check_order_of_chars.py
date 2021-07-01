# -*- coding: utf-8 -*-
"""
Created on Sat May 29 08:32:52 2021

@author: dimpl
"""

# Check order of character in string using OrderedDict()
# =============================================================================
# Input:
# string = "engineers rock"
# pattern = "er";
# Output: true
# Explanation:
# All 'e' in the input string are before all 'r'.
#
# Input:
# string = "engineers rock"
# pattern = "egr";
# Output: false
# Explanation:
# There are two 'e' after 'g' in the input string.
#
# Input:
# string = "engineers rock"
# pattern = "gsr";
# Output: false
# Explanation:
# There are one 'r' before 's' in the input string.
# =============================================================================

# Method 2: Without Dictionary
input = "engineers rock"
pattern = "en"
# found = ""
flag = False
ctr = 0

for i in input:
    if i in pattern:
        if i == pattern[ctr] or i == pattern[ctr - 1]:
            ctr += 1
            # found += i
            if ctr == len(pattern):
                flag = True
                print("order found")
                break
        else:
            break

if flag == False:
    print("order not found")


# Method 1: Wrong
# from collections import OrderedDict

# input = 'engineers rock'
# pattern = 'egr'
# flag=False

# # create empty OrderedDict
# # output will be like {'a': None,'b': None, 'c': None}
# dict=OrderedDict.fromkeys(input)
# print(dict)

# ptrlen = 0
# found=[]
# for key,val in dict.items():
#     if key in pattern:
#         if key!=pattern[ptrlen]:
#             break
#         else:
#             ptrlen+=1

#     # check if we have traverse completevpattern string
#     if(ptrlen==len(pattern)):
#         flag=True
#         print('order found')
#         break
# if flag==False:
#     print('order not found')
