# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:05:00 2021

@author: ANIL
"""
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line.rstrip())
