# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:16:05 2021

@author: ANIL
"""

'''
Merging two Dictionaries
'''

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

#method-1
dict1.update(dict2)
print(dict1)

#method-2
dict3 = {**dict1, **dict2}
print(dict3)


#method-3 pthon>=3.9
#dict3 = dict1 | dict2
#print(dict3)
