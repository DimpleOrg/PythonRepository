# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:19:18 2021

@author: ANIL
"""


class Restaurant:
    """ Restaurant class """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'The restaurant name is {self.restaurant_name}.')
        print(f'The cuisine type is {self.cuisine_type}.')

    def open_restaurant(self):
        print('The restaurant is oepn.')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, val):
        self.number_served += val


restaurant_one = Restaurant('Holiday Inn', 'Italian')
restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()

print(f'The number of customer servered: {restaurant_one.number_served}')
restaurant_one.set_number_served(100)
print(f'The number of customer servered: {restaurant_one.number_served}')
restaurant_one.increment_number_served(10)
print(f'The number of customer servered: {restaurant_one.number_served}')
