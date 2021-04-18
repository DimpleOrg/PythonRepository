# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 07:30:15 2021

@author: dimpl
"""

# Python | Cloning or Copying a list

# Using slicing technique
li1 = [4, 8, 2, 10, 15, 18]
li2=li1[:]
print(li2)


# Using the extend() method
list1 = [4, 8, 2, 10, 15, 18]
list2=[]
list2.extend(list1)
print(list2)


# Using the list() method
my_list1 = [4, 8, 2, 10, 15, 18]
my_list2=list(my_list1)
print(my_list2)


# Using the method of Shallow Copy
import copy

my_lista = [4, 8, 2, 10, 15, 18]
my_listb=copy.copy(my_lista)
print(my_listb)


# Using the method of Deep Copy
import copy

my_listc = [4, 8, 2, 10, 15, 18]
my_listd=copy.deepcopy(my_listc)
print(my_listd)


# Using Copy method
my_listg = [4, 8, 2, 10, 15, 18]
my_listh=my_listg.copy()
print(my_listh)


# Using list comprehension
my_liste = [4, 8, 2, 10, 15, 18]
my_listf=[x for x in my_liste]
print(my_listf)

