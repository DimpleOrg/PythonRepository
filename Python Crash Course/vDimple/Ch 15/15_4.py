# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 08:04:57 2021

@author: dimpl
"""

import matplotlib.pyplot as plt
from random_walk_15_4 import RandomWalk

# Make a random walk.
rw = RandomWalk(5000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
# fig, ax = plt.subplots(figsize=(15, 9))
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=3)
plt.show()
