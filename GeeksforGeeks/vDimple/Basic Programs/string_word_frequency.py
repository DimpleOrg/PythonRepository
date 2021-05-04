# -*- coding: utf-8 -*-
"""
Created on Tue May  4 07:36:20 2021

@author: dimpl
"""

# Words Frequency in String
# Input : test_str = ‘Gfg is best’
# Output : {‘Gfg’: 1, ‘is’: 1, ‘best’: 1}

# Input : test_str = ‘Gfg Gfg Gfg’
# Output : {‘Gfg’: 3}

# Method 1: count()+split()
test_str = "Gfg is best Gfg"
ctr = {each: test_str.count(each) for each in test_str.split()}
print(ctr)


# Method 2 : counter()+split()
from collections import Counter

test_str = "Gfg Gfg Gfg"
ctr1 = Counter(test_str.split())
print(dict(ctr1))
