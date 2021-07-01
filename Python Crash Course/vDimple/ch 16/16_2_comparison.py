# -*- coding: utf-8 -*-
"""
Created on Fri May  7 07:57:53 2021

@author: dimpl
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates1, highs1, lows1 = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high1 = int(row[5])
            low1 = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates1.append(current_date)
            highs1.append(high1)
            lows1.append(low1)

# Plot the high and low temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots(nrows=2)
ax[0].set_ylim([10, 150])
ax[0].plot(dates1, highs1, c="red", alpha=0.5)
ax[0].plot(dates1, lows1, c="blue", alpha=0.5)
ax[0].fill_between(dates1, highs1, lows1, facecolor="blue", alpha=0.1)

# Format plot.
ax[0].set_title("Daily Sitka high and low temperatures - 2018", fontsize=24)
# plt.title("Daily high temperatures, July 2018", fontsize=24)
# ax[0].xlabel("", fontsize=16)
# fig.autofmt_xdate()
# ax[0].ylabel("Temperature (F)", fontsize=16)
ax[0].tick_params(axis="both", which="major", labelsize=16)
# plt.show()


filename = "death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates2, highs2, lows2 = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high2 = int(row[5])
            low2 = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates2.append(current_date)
            highs2.append(high2)
            lows2.append(low2)

# Plot the high and low temperatures.
plt.style.use("seaborn")
# fig, ax = plt.subplots()
ax[1].set_ylim([10, 150])
ax[1].plot(dates2, highs2, c="red", alpha=0.5)
ax[1].plot(dates2, lows2, c="blue", alpha=0.5)
ax[1].fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)

# Format plot.
ax[1].set_title("Daily Death Valley high and low temperatures - 2018", fontsize=24)
# plt.title("Daily high temperatures, July 2018", fontsize=24)
# plt.xlabel("", fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
