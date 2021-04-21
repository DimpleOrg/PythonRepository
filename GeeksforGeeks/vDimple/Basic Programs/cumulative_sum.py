# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:33:58 2021

@author: dimpl
"""

# Python program to find Cumulative sum of a list

# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]

# Input : list = [4, 10, 15, 18, 20]
# Output : [4, 14, 29, 47, 67]

list1 =[4, 10, 15, 18, 20]
res=[]
sum1=0
# for x in list1:
#     sum1+=x
#     res.append(sum1)
    
# another way to do this using list comprehension.
res=[sum(list1[0:i]) for i in range(1,len(list1)+1)]    

print(*res)