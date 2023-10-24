import csv
import matplotlib.pyplot as plt


filename = 'data/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get high temperatures from this file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

    print(highs)

    # Plot the high temperatures
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(highs, c='red')

    plt.show()