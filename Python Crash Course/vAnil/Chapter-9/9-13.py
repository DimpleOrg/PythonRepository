# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:59:12 2021

@author: ANIL
"""
from random import randint


class Die:
    """Die Class"""

    def __init__(self, sides=6):
        self.sides = sides

    def rool_die(self):
        print(randint(1, self.sides))


die = Die()
die.rool_die()

die = Die(10)
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()

die = Die(20)
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
die.rool_die()
