import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'data/lwd_weer.csv'
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
            for index, column_header in enumerate(header_row):
                if column_header == 'TMAX':
                    high = int(row[index])
            high_celsius = (high - 32) / 1.8

            for index, column_header in enumerate(header_row):
                if column_header == 'TMIN':
                    index_min = index
            low_fahr = int(row[index_min])
            low_celsius = (low_fahr - 32) / 1.8

        except ValueError:
            print(f"Missing data for {current_date}")

        else:
            dates.append(current_date)
            highs.append(high_celsius)
            lows.append(low_celsius)

    # Plot the high temperatures
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)

    # Format plot
    plt.style.use('seaborn-v0_8')
    for column_header in header_row:
        if column_header == 'NAME':
            town = row[1].capitalize()
    plt.title(f"Hoogste en laagste temperaturen 2023\n{town}.", fontsize='20')
    plt.xlabel(' ', fontsize='16')
    fig.autofmt_xdate()
    plt.ylabel("Temperatuur (C)", fontsize='16')
    plt.tick_params(axis='both', which='major', labelsize='16')
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    plt.show()

