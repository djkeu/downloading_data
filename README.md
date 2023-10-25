# downloading_data

Python crash course
Project 2: Data visualization

# Chapter 16: Downloading data, p.333

# The CSV file format, p.334
Parsing the CSV File Headers, p.334
    sitka_highs.py
Printing the headers and their positions, p.335
Extracting and reading data, p.336
Plotting data in a temperature chart, p.336
The datetime module, p.337
Plotting dates, p.338
Plotting a longer timeframe, p.340
Plotting a second data series, p.340
    sitka_highs_lows.py
Shading an area in the chart, p.342
Error checking, p.343
    death_valley_highs_lows.py
Downloading your own data, p.345
    https://www.ncdc.noaa.gov/cdo-web/
Plot temperatures Leeuwarden from 3495766.csv


# Try it yourself, p.346

## ToDo: 16-1. Sitka Rainfall: 
    Sitka is in a temperate rainforest, so it gets a fair amount of rainfall. In the data file sitka_weather_2018_simple.csv is a header called PRCP, which represents daily rainfall amounts. Make a visualization focusing on the data in this column. You can repeat the exercise for Death Valley if you’re curious how little rainfall occurs in a desert

## ToDo: 16-2. Sitka–Death Valley Comparison: 
    The temperature scales on the Sitka and Death Valley graphs reflect the different data ranges. To accurately compare the temperature range in Sitka to that of Death Valley, you need identical scales on the y-axis. Change the settings for the y-axis on one or both of the charts in Figures 16-5 and 16-6. Then make a direct comparison between temperature ranges in Sitka and Death Valley (or any two places you want to compare).

## ToDo: 16-3. San Francisco: 
    Are temperatures in San Francisco more like tempera-
    tures in Sitka or temperatures in Death Valley? Download some data for San Francisco, and generate a high-low temperature plot for San Francisco to make a comparison.

## ToDo: 16-4. Automatic Indexes: 
    In this section, we hardcoded the indexes corresponding to the TMIN and TMAX columns. Use the header row to determine the indexes for these values, so your program can work for Sitka or Death Valley. Use the station name to automatically generate an appropriate title for your graph
    as well.

## ToDo: 16-5. Explore: 
    Generate a few more visualizations that examine any other weather aspect you’re interested in for any locations you’re curious about.

