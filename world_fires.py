import csv

from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    lats, longs, brights = [], [], []

    for row in reader:
        for index, column_header in enumerate(header_row):
            if column_header == 'latitude':
                lat = row[index]

            if column_header == 'longitude':
                long = row[index]

            if column_header == 'bright_ti4':
                bright = row[index]

        lats.append(lat)
        longs.append(long)
        brights.append(bright)
