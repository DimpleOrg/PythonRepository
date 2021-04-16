# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:11:14 2021

@author: ANIL
"""
import matplotlib.pyplot as plt

from random_walk_15_4 import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(5000)
    rw.fill_walk()
    
    # Set the size of the plotting window.
    plt.figure(dpi=128, figsize=(10, 6))
    
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
        
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=75)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=75)
        
    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
        
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
