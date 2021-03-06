# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:27:27 2021

@author: ANIL
"""


class Priviliges:
    """Store user priviliges"""

    def __init__(self, priviliges):
        self.privileges = priviliges

    def show_privileges(self):
        print(f'Priviliges: {self.privileges}')


class User:
    """User Information"""

    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.user_info['first_name'] = self.first_name
        self.user_info['last_name'] = self.last_name

    def dsecribe_user(self):
        print(f'\n{self.first_name.title()} {self.last_name.title()}')
        print(self.user_info)


class Admin(User):
    """ Admin class"""

    def __init__(self, first_name, last_name, privileges, **user_info, ):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Priviliges(privileges)


p_list = ['can add post', 'can ban user', 'can delete post']
user1 = Admin('Anil', 'Kumar', p_list,  email='a@gmail.com', dob='May-1')
user1.dsecribe_user()
user1.privileges.show_privileges()
