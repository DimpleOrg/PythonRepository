# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:50:40 2021

@author: dimpl
"""

# Simple interest

principle = 1000
rate = 5
time = 2
si = (principle*rate*time)/100

# Compound interest
# =============================================================================
# Formula to calculate compound interest annually is given by:
#
# A = P(1 + R/100) t
# Compound Interest = A – P
# Where,
# A is amount
# P is principle amount
# R is the rate and
# T is the time span
# =============================================================================

amount = principle*pow(1 + (rate/100), time)
compound_interest = amount-principle
