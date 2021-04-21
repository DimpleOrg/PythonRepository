# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:51:05 2021

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
        print('The restaurant is oepn.')


class IceCreamStand(Restaurant):
    """Ice Cream Stand - Restaurant"""

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f'Ice cream flvors: {self.flavors}')
