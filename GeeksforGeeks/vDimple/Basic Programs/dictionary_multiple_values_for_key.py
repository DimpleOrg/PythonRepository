# -*- coding: utf-8 -*-
"""
Created on Sun May 30 23:59:11 2021

@author: dimpl
"""

# How to create a dictionary where a key is formed using inputs?
# Let us consider an example where have an equation for three input variables,
# x, y and z. We want to store values of equation for different input triplets.

# Example 1:
# Python code to demonstrate a dictionary with multiple inputs in a key.

dict = {}
x, y, z = 1, 2, 3
dict[x, y, z] = x + y + z

x, y, z = 3, 4, 5
dict[x, y, z] = x + y + z

print(dict[x, y, z])


# Example 2:
places = {("19.07'53.2", "72.54'51.0"): "Mumbai", ("28.33'34.1", "77.06'16.6"): "Delhi"}

print("\r")
print(places)

lat = []
long = []
plc = []
for i in places:
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i[0], i[1]])

print("\r")
print(lat)
print(long)
print(plc)
