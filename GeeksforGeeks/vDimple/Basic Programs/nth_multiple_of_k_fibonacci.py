# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:46:08 2021

@author: dimpl
"""

# =============================================================================
# Given two integers n and k. Find position the n\’th multiple of K in the Fibonacci series.
# Examples:
#
# Input : k = 2, n = 3
# Output : 9
# 3\'rd multiple of 2 in Fibonacci Series is 34
# which appears at position 9.
#
# Input  : k = 4, n = 5
# Output : 30
# 5\'th multiple of 5 in Fibonacci Series is 832040
# which appears at position 30.

# Fibonacci Series(F) : 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040… (neglecting the first 0).

# An Efficient Solution is based on below interesting property.
# Fibonacci series is always periodic under modular representation. Below are examples.
#
# F (mod 2) = 1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,
#             1,1,0,1,1,0,1,1,0,1,1,0,1,1,0
# Here 0 is repeating at every 3rd index and
# the cycle repeats at every 3rd index.
#
# F (mod 3) = 1,1,2,0,2,2,1,0,1,1,2,0,2,2,1,0
#             ,1,1,2,0,2,2,1,0,1,1,2,0,2,2
# Here 0 is repeating at every 4th index and
# the cycle repeats at every 8th index.
# =============================================================================


k = 2
n = 3
fib_numbers = [1, 1]
multiples = {}
flag = True


while flag:
    a = fib_numbers[-1]
    b = fib_numbers[-2]
    result = a+b
    fib_numbers.append(result)
    if(result % k == 0):
        if k not in multiples:
            multiples[k] = []
        multiples[k].append(result)

        if len(multiples[k]) == n:
            print(len(fib_numbers))
            flag = False

# --------------------METHOD 2----------------------------


fib_numbers = [1, 1]
while True:
    a = fib_numbers[-1]
    b = fib_numbers[-2]
    result = a+b
    fib_numbers.append(result)
    if(result % k == 0):
        pos = len(fib_numbers)
        print(pos*n)
        break
