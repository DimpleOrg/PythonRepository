# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:20:51 2021

@author: dimpl
"""

# Program to print if the string contains all vowels 'a,e,i,o,u' or not

string = "SEEquoiaL"
vowels = {"a", "e", "i", "o", "u"}
set_a = set({})
for i in string.lower():
    if i in vowels:
        set_a.add(i)

if vowels == set_a:
    print("It has all vowels")
else:
    print("it doesn't have all vowels")

# Method 2:
string1 = string.lower()
res = [
    string1.count("a"),
    string1.count("e"),
    string1.count("i"),
    string1.count("o"),
    string1.count("u"),
]
if res.count(0) > 0:
    print("it doesn't have all vowels")
else:
    print("it has all vowels")


# Method 3:
if len(set(string.lower()).intersection("aeiou")) >= 5:
    print("It has all vowels")
else:
    print("it doesn't have all vowels")
