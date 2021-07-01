# -*- coding: utf-8 -*-
"""
Created on Sun May 30 11:05:31 2021

@author: dimpl
"""


from collections import OrderedDict

input = "engineers rock"
pattern = "en"

ordered_dict = OrderedDict()
pos = 0
for i in input:

    if i in ordered_dict.keys():
        ordered_dict[i].append(pos)
    else:
        ordered_dict[i] = [pos]
    pos += 1

prev = None
res = "Found"
for i in pattern:
    if i in ordered_dict.keys():
        firstindex = ordered_dict[i][0]

        if prev != None:
            lastindex = ordered_dict[prev][-1]
            if lastindex > firstindex:
                res = "Not Found"
                break
    else:
        res = "not found"
        break
    prev = i

print(res)
print(ordered_dict)
