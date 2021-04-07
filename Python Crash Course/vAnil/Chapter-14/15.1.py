# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:09:27 2021

@author: ANIL
"""

'''
15-1. Cubes: A number raised to the third power is a cube. Plot the first five 
cubic numbers, and then plot the first 5000 cubic numbers.
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,8,27,64,125]




plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
ax.scatter(x, y, s=10)



x = [ val  for val in range(1,5001)]
y = [val**3 for val in range(1,5001)]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
ax.scatter(x, y, s=10)