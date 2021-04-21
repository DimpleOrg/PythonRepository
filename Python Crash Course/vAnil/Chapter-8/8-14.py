# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:27:58 2021

@author: ANIL
"""


def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


built_car = make_car('honda', 'civic', color='blue', tow_package=True)
print(built_car)
