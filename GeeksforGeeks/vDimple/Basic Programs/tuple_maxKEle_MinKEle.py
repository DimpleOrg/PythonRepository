# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 06:16:49 2021

@author: dimpl
"""

# Python – Maximum and Minimum K elements in Tuple
# Input : test_tup = (3, 7, 1, 18, 9), k = 2
# Output : (3, 1, 9, 18)

test_tup = (3, 7, 1, 18, 9, 27, 53, 72)
k = 2

temp = sorted(test_tup)

ctr = 0
while ctr < k:
    print(temp[ctr])
    ctr += 1

while ctr > 0:
    print(temp[-ctr])
    ctr -= 1

print("****************************")
# Method2:

res = tuple(temp[:k] + temp[-k:])
print(res)
