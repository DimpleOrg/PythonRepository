# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:23:41 2021

@author: ANIL
"""


class User:
    """User Information"""

    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.user_info['first_name'] = self.first_name
        self.user_info['last_name'] = self.last_name
        self.login_attempts = 0

    def dsecribe_user(self):
        print(f'\n{self.first_name.title()} {self.last_name.title()}')
        print(self.user_info)

    def incrment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('Anil', 'Kumar', email='a@gmail.com', dob='May-1')
user1.dsecribe_user()
user2 = User('Raj', 'Sing', email='b@gmail.com', dob='May-10')
user2.dsecribe_user()
user3 = User('Disha', 'lal', email='disha@gmail.com', dob='Jan-10')
user3.dsecribe_user()

print(f'\n\nlogin attempts: {user1.login_attempts}')
user1.incrment_login_attempts()
user1.incrment_login_attempts()
user1.incrment_login_attempts()
user1.incrment_login_attempts()
user1.incrment_login_attempts()
print(f'\n\nlogin attempts: {user1.login_attempts}')
user1.reset_login_attempts()
print(f'\n\nReset the login attempts: {user1.login_attempts}')
