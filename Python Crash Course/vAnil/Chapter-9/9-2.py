# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:56:33 2021

@author: ANIL
"""


class Restaurant:
    """ Restaurant class """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The restaurant name is {self.restaurant_name}.')
        print(f'The cuisine type is {self.cuisine_type}.')

    def open_restaurant(self):
        print('The restaurant is oepn.\n')


restaurant_one = Restaurant('Holiday Inn', 'Italian')
restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()
restaurant_two = Restaurant('Alinea', 'New-Style')
restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()
restaurant_three = Restaurant('The Berghoff', 'German')
restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()
