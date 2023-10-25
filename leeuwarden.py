import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/3495766.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates, and high and low temperatures from this file
    dates, highs, lows = [], [], []    
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high_fahr = int(row[3])
            high_celsius = (high_fahr - 32) / 1.8
            low_fahr = int(row[4])
            low_celsius = (low_fahr -32) / 1.8
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high_celsius)
            lows.append(low_celsius)

    # Plot the high temperatures
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot
    plt.title("Daily high and low temperatures - 2023\nLeeuwarden, Frl", fontsize='20')
    plt.xlabel(' ', fontsize='16')
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize='16')
    plt.tick_params(axis='both', which='major', labelsize='16')

    plt.show()
