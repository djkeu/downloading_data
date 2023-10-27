import csv

from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    lats, lons, brights = [], [], []

    for row in reader:
        for index, column_header in enumerate(header_row):
            if column_header == 'latitude':
                lat = row[index]

            if column_header == 'longitude':
                long = row[index]

            if column_header == 'bright_ti4':
                bright = row[index]

        lats.append(lat)
        lons.append(long)
        brights.append(bright)

# Map the fires
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': 2,
        'color': 'red',
    }
}]

my_layout = Layout(title="Global fires")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
