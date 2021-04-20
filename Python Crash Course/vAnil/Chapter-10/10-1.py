# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:53:43 2021

@author: ANIL
"""
with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
