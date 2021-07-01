# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 23:10:02 2021

@author: dimpl
"""

# Order Tuples by List

# Input : test_list = [(‘Gfg’, 10), (‘best’, 3), (‘CS’, 8), (‘Geeks’, 7)], ord_list = [‘Geeks’, ‘best’, ‘CS’, ‘Gfg’]
# Output : [(‘Geeks’, 7), (‘best’, 3), (‘CS’, 8), (‘Gfg’, 10)]

test_list = [("Gfg", 10), ("best", 3), ("CS", 8), ("Geeks", 7), ("Geeks", 9)]
ord_list = ["Geeks", "best", "CS", "Gfg"]

# Method #1 : Using dict() + list comprehension
temp = dict(test_list)
res = [(item, temp[item]) for item in ord_list]
print(res)


# Method #2 : Using setdefault() + sorted() + lambda
# temp = dict()
# for idx, val in enumerate(ord_list):
#     temp.setdefault(val, []).append(idx)
# res1 = sorted(test_list, key=lambda x: temp[x[0]].pop())
# print(res1)
