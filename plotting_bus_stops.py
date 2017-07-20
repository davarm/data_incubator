from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, Square, Triangle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)
import pandas as pd

#----------------------------------
# Read the Brisbane city council bus stop dataset and save the lats and longs of each stop
# Not very large, therefor just ead into a pandas dataframe
#----------------------------------
df          = pd.read_csv('bus_stop_locations.csv',sep = ',', skipinitialspace = False)



#----------------------------------
# DROP SCHOLL BUS STOPS
#----------------------------------
df     = df.loc[df['BUS_STOP_TYPE'] != ('District')]
df     = df.reset_index(drop=True)


#----------------------------------
# Define df for 'PREMIUM'
#----------------------------------
premium_df     = df.loc[df['BUS_STOP_TYPE'] == ('Premium')]
premium_df     = premium_df.reset_index(drop=True)

#----------------------------------
# Define df for 'Intermediate'
#----------------------------------
intermediate_df     = df.loc[df['BUS_STOP_TYPE'] == ('Intermediate')]
intermediate_df     = intermediate_df.reset_index(drop=True)


#----------------------------------
# Define df for all other / regular df
#----------------------------------
strng= "Premium"
strng1= "Intermediate"
regular_df = df.query('BUS_STOP_TYPE != @strng and BUS_STOP_TYPE != @strng1')
regular_df     = regular_df.reset_index(drop=True)

#----------------------------------
# Define the longitude and latitude into lists
#----------------------------------

premium_lng = premium_df['LONGITUDE'].tolist()
premium_lat = premium_df['LATITUDE'].tolist()

intermediate_lng = intermediate_df['LONGITUDE'].tolist()
intermediate_lat = intermediate_df['LATITUDE'].tolist()

regular_lng = regular_df['LONGITUDE'].tolist()
regular_lat = regular_df['LATITUDE'].tolist()


#----------------------------------
# The longitude and latitude coordinates for Brisabne, QLD AUS
#----------------------------------
map_options = GMapOptions(lat=-27.4698, lng=153.0251, map_type="roadmap", zoom=11)

## LONG AND LAT FOR BRISBANE
plot = GMapPlot(
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options
)
plot.title.text = "Brisbane"

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:
plot.api_key = "AIzaSyBYb-QJcfGrR4y0X0Mx7XG3l4tnQqZAaBw"
#Google APIkey



#----------------------------------
# For PREMIUM BUS STOPS
#----------------------------------
source = ColumnDataSource(
    data=dict(
        lat=premium_lat,
        lon=premium_lng,
    )
)

circle = Circle(x="lon", y="lat", size=6, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

#----------------------------------
# For Intermediate Bus stops
#----------------------------------
source = ColumnDataSource(
    data=dict(
        lat=intermediate_lat,
        lon=intermediate_lng,
    )
)

square = Square(x="lon", y="lat", size=6, fill_color="red", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, square)

#----------------------------------
# For Regular Bus stops
#----------------------------------
source = ColumnDataSource(
    data=dict(
        lat=regular_lat,
        lon=regular_lng,
    )
)

triangle = Triangle(x="lon", y="lat", size=6, fill_color="green", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, triangle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("gmap_plot.html")
show(plot)