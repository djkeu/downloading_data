import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, collumn_header in enumerate(header_row):
        print(index, collumn_header)

    dates, rainfall = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = float(row[3]) * 10
        dates.append(current_date)
        rainfall.append(high)

    # print(rainfall)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='blue', linewidth='0.5')

plt.title("Rainfall in Sitka 2018")
plt.ylabel('Rain (mm)')
fig.autofmt_xdate()

plt.show()