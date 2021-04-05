# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:55:46 2021

@author: ANIL
"""

prinicpal = 100
time = 10
interestRate = 7

compound_interest = prinicpal * pow((1 + interestRate/100), time)

print(f'Compound Intereset is {compound_interest - prinicpal}')