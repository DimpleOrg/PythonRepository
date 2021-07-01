# -*- coding: utf-8 -*-
"""
Created on Sun May 30 23:41:08 2021

@author: dimpl
"""

# Handling missing keys in Python dictionaries

# Method 1 : Using get()
country_code = {"India": "0091", "Australia": "0025", "Nepal": "00977"}

# search dictionary for country code of India
print(country_code.get("India"))
print(country_code.get("Japan"))
print(country_code.get("Japan", "Not Found"))

print("***********************")
# Method 2 : Using setdefault()

# setdefault(key, def_value) works in a similar way as get(), but the difference
#  is that each time a key is absent, a new key is created with the def_value
#  associated to the key passed in arguments.

country_code = {"India": "0091", "Australia": "0025", "Nepal": "00977"}

# print(country_code['Japan'])    # will error out

country_code.setdefault("Japan", "No value for Japan")

print(country_code["India"])
print(country_code["Japan"])

print("***********************")

# Method 3 : Using defaultdict

# “defaultdict” is a container that is defined in module named “collections“. It
# takes a function(default factory) as its argument. By default, default factory
# is set to “int” i.e 0. If a key is not present is defaultdict, the default factory
# value is returned and displayed. It has advantages over get() or setdefault().

# A default value is set at the declaration. There is no need to invoke the function
# again and again and pass similar value as arguments. Hence saving time.
# The implementation of defaultdict is faster than get() or setdefault().

# importing "collections" for defaultdict
import collections

# declaring defaultdict
# sets default value 'Key Not found' to absent keys

default_dic = collections.defaultdict(lambda: "Key not found")

default_dic["a"] = 1
default_dic["f"] = 2

print(default_dic["f"])
print(default_dic["b"])
