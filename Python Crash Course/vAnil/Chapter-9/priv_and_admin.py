# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:57:06 2021

@author: ANIL
"""

from user import User


class Priviliges:
    """Store user priviliges"""

    def __init__(self, priviliges):
        self.privileges = priviliges

    def show_privileges(self):
        print(f'Priviliges: {self.privileges}')


class Admin(User):
    """ Admin class"""

    def __init__(self, first_name, last_name, privileges, **user_info, ):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Priviliges(privileges)
