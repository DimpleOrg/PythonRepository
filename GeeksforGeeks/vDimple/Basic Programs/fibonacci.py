# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:11:02 2021

@author: dimpl
"""
import math

# Python Program for n-th Fibonacci number
a = 1
b = 2
number = int(input("Please enter n for nth fibonacco number: "))
if number == 1:
    print(a)
elif number == 2:
    print(b)
else:
    var = 3
    while var <= number:
        result = a+b
        # print(result)
        a = b
        b = result
        var += 1
    print(result)

# Python Program for How to check if a given number is Fibonacci number?
# A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4)
# is a perfect square

number = int(input("Enter a number: "))
var1 = math.sqrt(5*pow(number, 2)+4)
var2 = math.sqrt(5*pow(number, 2)-4)
if var1 == int(var1) or var2 == int(var2):
    print("Yes it's a fibonacci number.")
else:
    print("No it's not a fibonacci number.")
