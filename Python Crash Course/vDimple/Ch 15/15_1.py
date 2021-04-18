# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:33:17 2021

@author: dimpl
"""

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5,6]
cubes = [1, 8,27,64,125,216]
plt.style.use('ggplot')

# subplots() function - This function can generate one or more plots in the same figure.
# The variable fig represents the entire figure or collection of plots that
# are generated. 
# The variable ax represents a single plot in the figure and is
# the variable we’ll use most of the time.
fig, ax = plt.subplots()
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
#ax.plot(input_values,cubes,linewidth=3)
ax.scatter(input_values,cubes,s=100)

# The variable fig represents the entire figure or collection of plots that
# are generated. The variable ax represents a single plot in the figure and is
# the variable we’ll use most of the time.
plt.show()

# Saving your plots automatically
plt.savefig('squares_plot.png', bbox_inches='tight')