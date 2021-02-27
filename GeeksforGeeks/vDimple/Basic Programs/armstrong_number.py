# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:02:59 2021

@author: dimpl
"""

# Area of circle

radius = 5
area = 3.14*pow(radius, 2)

# Armstrong number
# Example:

# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153

# Input : 120
# Output : No
# 120 is not a Armstrong number.
# 1*1*1 + 2*2*2 + 0*0*0 = 9

# Input : 1253
# Output : No
# 1253 is not a Armstrong Number
# 1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723

number = int(input("Enter number: "))
number_copy = number
digits = []
while number > 0:
    rem = number % 10
    digits.append(rem)
    number = number//10

result = 0
for each in digits:
    result += pow(each, len(digits))

if result == number_copy:
    print("This is an armstrong number.")
else:
    print("This is not an armstrong number.")
