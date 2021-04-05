# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:02:16 2021

@author: dimpl
"""

# =============================================================================
# Given multiple numbers and a number n, the task is to print the remainder after
# multiply all the number divide by n.
# Examples:
#
# Input: arr[] = {100, 10, 5, 25, 35, 14},
# n = 11
# Output: 9
# 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9
#
# Naive approach: First multiple all the numbers then take % by n then find the
# remainder, But in this approach, if the number is maximum of 2 ^ 64 then it
# gives the wrong answer.
# Approach that avoids overflow: First take a remainder or individual number like
#  arr[i] % n. Then multiply the remainder with the current result. After
#  multiplication, again take the remainder to avoid overflow. This works because
#  of the distributive properties of modular arithmetic.
#  (a * b) % c = ((a % c) * (b % c)) % c
#
# =============================================================================

arr = [100, 10, 5, 25, 35, 14]
n = 11

mult = 1
for i in arr:
    mult *= (i % n)

print(mult % n)
