# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:02:41 2021

@author: ANIL
"""

def IsArmstrong(num):
    digits = []
    x = num
    while x > 0:
        digits.append(x%10)
        x = x//10


    total = 0
    numDigits = len(digits)
    
    for digit in digits:
        total += pow(digit, numDigits)

    
    if num == total:
        return True
    else:
        return False
    

num = 153
print(f'{num} is Armstrong number: {IsArmstrong(num)}')