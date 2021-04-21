# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:40:02 2021

@author: dimpl
"""

# Python | Sum of number digits in List

# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

# Method #1 : Using loop + str()
list1=[12, 67, 98, 34]
res=[]
for x in list1:
    sum=0
    for digit in str(x):
        sum+=int(digit)
    res.append(sum)

print("The original list is : " ,(list1))
print ("List Integer Summation : " + str(res))