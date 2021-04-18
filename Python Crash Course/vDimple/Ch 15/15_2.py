# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:03:15 2021

@author: dimpl
"""
import matplotlib.pyplot as plt

x_values=range(1,5001)
y_values=[x**3 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Cube of Value", fontsize=24)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=24)
ax.scatter(x_values,y_values,c=y_values, cmap=plt.cm.plasma,linewidth=3)

# Set the range for each axis.
#ax.axis([0, 1100, 0, 1100000])
plt.show()

# Saving your plots automatically
plt.savefig('squares_plot.png', bbox_inches='tight')