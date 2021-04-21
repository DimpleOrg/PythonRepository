# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:36:55 2021

@author: ANIL
"""
from printing_functions import make_car
from printing_functions import make_car as mc
import printing_functions as pf

built_car = make_car(
    'honda', 'civic', color='blue', tow_package=True)
print(built_car)

built_car = mc(
    'honda', 'civic', color='blue', tow_package=True)
print(built_car)

built_car = pf.make_car(
    'honda', 'civic', color='blue', tow_package=True)
print(built_car)
