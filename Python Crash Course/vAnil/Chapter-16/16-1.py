# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:30:57 2021

@author: ANIL
"""

'''
16-1. Sitka Rainfall: Sitka is in a temperate rainforest, so it gets a fair amount of 
rainfall. In the data file sitka_weather_2018_simple.csv is a header called PRCP, 
which represents daily rainfall amounts. Make a visualization focusing on the 
data in this column. You can repeat the exercise for Death Valley if you’re curious how little rainfall occurs in a desert.
'''

import csv

import matplotlib.pyplot as plt

#%matplotlib auto

filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    
    PRCP = []
    
    for row in reader:
        try:
            if row[3]:
                PRCP.append(float(row[3]))
        except ValueError:
            print('ERROR:', row[3])

plt.style.use('seaborn')
fig, ax = plt.subplots(nrows=2)
ax[0].set_title('Sitka Weather 2018 Simple', fontsize=24, color='red')
ax[0].plot(PRCP, c='red')

filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    
    PRCP = []
    
    for row in reader:
        try:
            if row[3]:
                PRCP.append(float(row[3]))
        except ValueError:
            print('ERROR:', row[3])

ax[1].set_title('Death Valley 2018 Simple', fontsize=24, color='green')
ax[1].plot(PRCP, c='green',label="death_valley_2018_simple")
fig.tight_layout()

