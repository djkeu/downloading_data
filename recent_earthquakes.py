import json

from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/all_day.json'
with open(filename) as f:
    all_data = json.load(f)

eq_dicts = all_data['features']

# Can't json.load downloaded .json file
