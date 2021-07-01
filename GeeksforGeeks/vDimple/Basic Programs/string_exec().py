# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:18:10 2021

@author: dimpl
"""

# Execute a String of Code in Python
# Input:
# code = """ a = 6+5
#            print(a)"""
# Output:
# 11

# Input:
# code = """ def factorial(num):
#                for i in range(1,num+1):
#                    fact = fact*i
#                return fact
#            print(factorial(5))"""
# Output:
# 120

code = """a = 6+5
print(a)"""

code1 = """def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    return fact
print(factorial(5))"""

exec(code)
exec(code1)
