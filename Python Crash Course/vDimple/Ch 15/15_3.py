# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 08:04:57 2021

@author: dimpl
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()
    
    # Plot the points in the walk.
    plt.style.use('classic')
    #fig, ax = plt.subplots(figsize=(15, 9))
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=3)
    
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.plasma,
    #            edgecolors='none', s=1)
    
    # Emphasize the first and last points.
    # ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    #           s=100)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break