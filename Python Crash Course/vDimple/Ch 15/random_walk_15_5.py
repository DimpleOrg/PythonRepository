# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:18:50 2021

@author: dimpl
"""
# =============================================================================
# A random walk is a path that has no clear direction but is determined
# by a series of random decisions, each of which is left entirely to chance. You
# might imagine a random walk as the path a confused ant would take if it
# took every step in a random direction.
# 316 Chapter 15
# Random walks have practical applications in nature, physics, biology,
# chemistry, and economics. For example, a pollen grain floating on a
# drop of water moves across the surface of the water because it’s constantly
# pushed around by water molecules. Molecular motion in a water drop is
# random, so the path a pollen grain traces on the surface is a random walk.
# 
# =============================================================================
from random import choice

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
        
    def get_step(self):
        # Decide which direction to go and how far to go in that direction.
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step
        
    def fill_walk(self):
        """Calculate all the points in the walk."""
        
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go, and how far to go in that direction.
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
        
            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)