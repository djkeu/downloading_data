import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sf_weather_2018.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print('missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    ax.plot(dates, lows, c='blue')

    plt.style.use('seaborn-v0_8')
    plt.title("San Francisco weather, 2018")
    plt.ylabel("Temperatures (F)")
    plt.tick_params(axis='y', which='major', labelsize=16)

    plt.show()
