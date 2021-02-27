# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:20:54 2021

@author: dimpl
"""

# Python Program for factorial of a number
number = int(input("enter a number to find its factorial: "))
print(f"Factorial of {number} is: ")
result = number
while number > 1:
    number -= 1
    result *= number

print(f"{result}")
