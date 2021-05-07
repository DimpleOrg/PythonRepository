# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:44:23 2021

@author: ANIL
"""

'''
16-2. Sitka–Death Valley Comparison: The temperature scales on the Sitka and 
Death Valley graphs reflect the different data ranges. To accurately compare 
the temperature range in Sitka to that of Death Valley, you need identical 
scales on the y-axis. Change the settings for the y-axis on one or both of the 
charts in Figures 16-5 and 16-6. Then make a direct comparison between 
temperature ranges in Sitka and Death Valley (or any two places you want to 
compare).
'''

import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.set_ylim([10,150])
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()