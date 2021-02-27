# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:20:38 2021

@author: dimpl
"""

# Maximum of two numbers in Python
number1 = int(input("enter 1st number: "))
number2 = int(input("enter 2nd number: "))
if number1 > number2:
    result = number1
else:
    result = number2
print(f"Greater of {number1} & {number2} is: {result}")
