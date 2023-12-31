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

If you want to download your own weather data, follow these steps:

1. Visit the NOAA Climate Data Online site at https://www.ncdc.noaa.gov/cdo-web/. In the Discover Data By section, click Search Tool. In the Select a Dataset box, choose Daily Summaries.

2. Select a date range, and in the Search For section, choose ZIP Codes. Enter the ZIP Code you’re interested in, and click Search.

3. On the next page, you’ll see a map and some information about the area you’re focusing on. Below the location name, click View Full Details, or click the map and then click Full Details.

4. Scroll down and click Station List to see the weather stations that are available in this area. Choose one of the stations, and click Add to Cart. This data is free, even though the site uses a shopping cart icon. In the
upper-right corner, click the cart.

5. In Select the Output, choose Custom GHCN-Daily CSV. Make sure the date range is correct, and click Continue.

6. On the next page, you can select the kinds of data you want. You can download one kind of data, for example, focusing on air temperature, or you can download all the data available from this station. Make your choices, and then click Continue.

7. On the last page, you’ll see a summary of your order. Enter your email address, and click Submit Order. You’ll receive a confirmation that your order was received, and in a few minutes you should receive another email with a link to download your data. The data you download will be structured just like the data we worked with in this section. It might have different headers than those you saw in this section. But if you follow the same steps we used here, you should be
able to generate visualizations of the data you’re interested in.


# Try it yourself, p.346

## 16-1. Sitka Rainfall: 
    Sitka is in a temperate rainforest, so it gets a fair amount of rainfall. In the data file sitka_weather_2018_simple.csv is a header called PRCP, which represents daily rainfall amounts. Make a visualization focusing on the data in this column. You can repeat the exercise for Death Valley if you’re curious how little rainfall occurs in a desert
        sitka_rainfall.py

## 16-2. Sitka–Death Valley Comparison: 
    The temperature scales on the Sitka and Death Valley graphs reflect the different data ranges. To accurately compare the temperature range in Sitka to that of Death Valley, you need identical scales on the y-axis. Change the settings for the y-axis on one or both of the charts in Figures 16-5 and 16-6. Then make a direct comparison between temperature ranges in Sitka and Death Valley (or any two places you want to compare).
        sitka_highs_lows.py
        death_valley_highs_lows.py

## 16-3. San Francisco: 
    Are temperatures in San Francisco more like tempera-
    tures in Sitka or temperatures in Death Valley? Download some data for San Francisco, and generate a high-low temperature plot for San Francisco to make a comparison.
        san_francisco_temperatures.py

## 16-4. Automatic Indexes: 
    In this section, we hardcoded the indexes corresponding to the TMIN and TMAX columns. Use the header row to determine the indexes for these values, so your program can work for Sitka or Death Valley. Use the station name to automatically generate an appropriate title for your graph
    as well.

## 16-5. Explore: 
    Generate a few more visualizations that examine any other weather aspect you’re interested in for any locations you’re curious about.
        leeuwarden.py


# Mapping global data sets: JSON format, p.347
Downloading earthquake data, p.347
Examining JSON data, p.347
    eq_explore_data.py
Making a list of all earthquakes, p.350
Extracting magnitudes, p.350
Extracting location data, p.351
Building a world map, p.351
A Different Way of Specifying Chart Data, p.353
Customizing marker size, p.353
Customizing marker colors, p.354
    eq_world_map.py
Other colorscales, p.356
    show_color_scales.py
Adding hover text, p.356
    eq_world_map.py


# Try it yourself, p.357

## 16-6. Refactoring: 
    The loop that pulls data from all_eq_dicts uses variables for the magnitude, longitude, latitude, and title of each earthquake before appending these values to their appropriate lists. This approach was chosen for clarity in how to pull data from a JSON file, but it’s not necessary in your code. Instead of using these temporary variables, pull each value from eq_dict and append it to the appropriate list in one line. Doing so should shorten the body of this loop to just four lines.

## 16-7. Automated Title: 
    In this section, we specified the title manually when defining my_layout, which means we have to remember to update the title every time the source file changes. Instead, you can use the title for the data set in the metadata part of the JSON file. Pull this value, assign it to a variable, and use this for the title of the map when you’re defining my_layout.

## 16-8. Recent Earthquakes: 
    You can find data files containing information about the most recent earthquakes over 1-hour, 1-day, 7-day, and 30-day periods online. Go to https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php and you’ll see a list of links to data sets for various time periods, focusing on earthquakes of different magnitudes. Download one of these data sets, and create a visualization of the most recent earthquake activity.
        recent_earthquakes.py

## 16-9. World Fires: 
    In the resources for this chapter, you’ll find a file called world_fires_1_day.csv. This file contains information about fires burning in different locations around the globe, including the latitude and longitude, and the brightness of each fire. Using the data processing work from the first part of this chapter and the mapping work from this section, make a map that shows which parts of the world are affected by fires. You can download more recent versions of this data at https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/. You can find links to the data in CSV format in the TXT section.
        global_fires.py
    