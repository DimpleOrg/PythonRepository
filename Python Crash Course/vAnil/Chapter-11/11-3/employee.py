# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 17:25:12 2021

@author: ANIL
"""


class Employee:
    """Employee Class"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_ammount=5000):
        self.annual_salary += raise_ammount
