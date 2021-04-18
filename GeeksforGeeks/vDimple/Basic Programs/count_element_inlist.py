# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 07:42:50 2021

@author: dimpl
"""

# Python | Count occurrences of an element in a list

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 16
print(lst.count(x))


# Counter method returns a dictionary with occurrences of all elements as a 
# key-value pair, where key is the element and value is the number of times 
# that element has occurred.
from collections import Counter

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
d=Counter(lst)
print(d)
print(d[x])