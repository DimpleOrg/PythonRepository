# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:34:59 2021

@author: ANIL
"""


def findWord(file_name, word):
    with open(file_name) as f:
        contents = f.read()
    return contents.lower().count(word)


print(findWord('hints_for_lovers.txt', 'the'))
print(findWord('little_masterpieces_of_science.txt', 'the'))
print(findWord('test_for_the_pearl.txt', 'the'))


print(findWord('hints_for_lovers.txt', 'the '))
print(findWord('little_masterpieces_of_science.txt', 'the '))
print(findWord('test_for_the_pearl.txt', 'the '))

print(findWord('hints_for_lovers.txt', ' the '))
print(findWord('little_masterpieces_of_science.txt', ' the '))
print(findWord('test_for_the_pearl.txt', ' the '))
