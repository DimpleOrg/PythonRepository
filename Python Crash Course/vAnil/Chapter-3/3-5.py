# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:56:17 2020

@author: ANIL
"""

guests = ['Einstein', 'Tesla', 'Newton']
print(f"Dear {guests[0]}, please come to my dinner.")
print(f"Dear {guests[1]}, please come to my dinner.")
print(f"Dear {guests[2]}, please come to my dinner.\n")
print(f"My guest {guests[0]}, can't make it to dinner.\n\n")

guests[0] = 'Rajesh Khanna'
print(f"Dear {guests[0]}, please come to my dinner.")
print(f"Dear {guests[1]}, please come to my dinner.")
print(f"Dear {guests[2]}, please come to my dinner.")
