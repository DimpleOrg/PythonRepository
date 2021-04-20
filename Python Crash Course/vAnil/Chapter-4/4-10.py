# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 20:09:11 2021

@author: ANIL
"""
cubes = [value**3 for value in range(1, 11)]

print("The first three itme in the list are:")
for cube in cubes[:3]:
    print(cube)

print("Three items from the middle of the list are:")
for cube in cubes[4:7]:
    print(cube)

print("The last three items in the list are:")
for cube in cubes[-3:]:
    print(cube)
