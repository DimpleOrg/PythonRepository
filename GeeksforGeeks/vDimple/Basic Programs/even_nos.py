# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 08:26:34 2021

@author: dimpl
"""

# Given a list of numbers, write a Python program to print all even numbers in given list.

list1=[1,2,4,58,3,36,23,0]
even_num= [x for x in list1 if x%2==0]
print(even_num)