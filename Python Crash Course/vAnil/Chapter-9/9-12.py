# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:58:18 2021

@author: ANIL
"""
from priv_and_admin import Admin

p_list = ['can add post', 'can ban user', 'can delete post']
user1 = Admin('Anil', 'Kumar', p_list,  email='a@gmail.com', dob='May-1')
user1.dsecribe_user()
user1.privileges.show_privileges()
