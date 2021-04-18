# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:28:50 2021

@author: dimpl
"""
# =============================================================================
# Given a list, print the value obtained after multiplying all numbers in a list.
# Examples:
#
#
# Input :  list1 = [1, 2, 3]
# Output : 6
# Explanation: 1*2*3=6
# =============================================================================

import math
from functools import reduce
import numpy
my_list = [1, 2, 3, 4]
mult = 1
for each in my_list:
    mult *= each
print(mult)

# -------------METHOD 2-----------------

my_list = [1, 2, 3, 4]
result = numpy.prod(my_list)
print(result)


# -------------METHOD 3-----------------
# =============================================================================
# Method 3 Using lambda function: Using numpy.array
# Lambda’s definition does not include a “return” statement, it always contains
# an expression that is returned. We can also put a lambda definition anywhere
# a function is expected, and we don’t have to assign it to a variable at all.
# This is the simplicity of lambda functions. The reduce() function in Python
# takes in a function and a list as an argument. The function is called with a
# lambda function and a list and a new reduced result is returned.
# =============================================================================


my_list = [1, 2, 3, 4]
result = reduce((lambda x, y: x*y), my_list)
print(result)

# -------------METHOD 4-----------------
# Method 4 Using prod function of math library: Using math.prod


my_list = [1, 2, 3, 4]
result = math.prod(my_list)
print(result)
