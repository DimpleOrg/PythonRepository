# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:26:56 2021

@author: dimpl
"""

import matplotlib.pyplot as plt
import csv

%matplotlib auto

filename = "santa_monica_climate.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get high temperatures from this file.
    rain = []
    for row in reader:
        if row[5] != "":
            prcp = float(row[5])
            rain.append(prcp)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(rain, c="red")
