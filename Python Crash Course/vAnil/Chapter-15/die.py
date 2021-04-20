# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:29:33 2021

@author: ANIL
"""

from random import randint

class Die:
    """A class representing a single die."""
 
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
 
    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)