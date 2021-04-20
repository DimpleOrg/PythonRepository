# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:37:20 2021

@author: ANIL
"""

'''
15-2. Colored Cubes: Apply a colormap to your cubes plot.
'''
import matplotlib.pyplot as plt

x = [ val  for val in range(1,5001)]
y = [val**3 for val in range(1,5001)]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
#ax.scatter(x, y, c='green',s=7)

ax.scatter(x, y, c=y, cmap=plt.cm.plasma, s=10)
plt.show()