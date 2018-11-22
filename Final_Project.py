#imports
from craigslist import CraigslistJobs, CraigslistHousing
import requests
import json
import matplotlib
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly
from plotly.graph_objs import *
import plotly.graph_objs as go
import cufflinks as cf
import googlemaps
import pandas as pd
import numpy as np

#Credentials to log in to plotly
plotly.tools.set_credentials_file(username='marc0274', api_key='8vaOF5Wla0Bzlvroc1SG')

#hardcoded variables
zipcode = 13210
radius = 7
places = ['apartment','duplex','house','loft']

#lists
latitude_list = []
longitude_list = []
syracuse_address =[]
geo = []
names = []


#Menu and Inputs

print("Welcome to:\n\n Syracuse University Home Finder")
print(" -------------------------------")


print("Please answer the following questions:")

while True:
    maxp = int(input("What is your Max Price?: "))
    if maxp >= 1:
        break
    else:
        print("Please Enter a valid number!")
        continue     
while True:
    bedrooms = int(input("How many Bedrooms would you perfer?: "))
    if bedrooms >= 1:
        break
    else:
        print("Please Enter a valid number!")
        continue 
while True:
    bathrooms = int(input("How many bathrooms would you like?: "))
    if bathrooms >= 1:
        break
    else:
        print("Please Enter a valid number!")
        continue  
while True:
    furnished = input("Would you want your home to be furnished? Enter y/n: ")
    if furnished == "y":
        furnished = True
        break
    elif furnished == "n":
        furnished = False
        break
    else:
        print("You should enter either \"y\" or \"n\": ")
        continue
while True:
    smoke = input("Would you want a smoke-free home? Enter y/n: ")
    if smoke == "y":
        smoke = True
        break
    elif smoke == "n":
        smoke = False
        break
    else:
        print("You should enter either \"y\" or \"n\": ")
        continue
while True:
    pets = input("Do you want a home that allows pets? Enter y/n: ")
    if pets == "y":
        pets = True
        break
    elif pets == "n":
        pets = False
        break
    else:
        print("You should enter either \"y\" or \"n\": ")
        continue





#Connect to Craigslist API and Customize search
syracuse = CraigslistHousing(site='syracuse', 
                       filters={'search_distance': radius, 'zip_code': zipcode, 'max_price': maxp, 'min_bedrooms': bedrooms,'max_bathrooms': bathrooms,'no_smoking': smoke,'is_furnished': furnished,'housing_type': places, 'cats_ok':pets, 'dogs_ok':pets  })

# Loop that takes the reults needed
for spot in syracuse.get_results(sort_by='newest' , geotagged= True, limit=15):
    syracuse_address.append(spot)



#loop to split longitude and latitude that in one index

for line in syracuse_address:
    
    if not line['geotag'] is None:
        latitude_list.append(line['geotag'][0])
        longitude_list.append(line['geotag'][1])
        names.append(line['name'] + line["where"] + line["price"])
    


#Prints what Craigslist returns
print(latitude_list)
print(names)
print(longitude_list)



#plotly Access Info and Design

mapbox_access_token = 'pk.eyJ1IjoibWFyYzAyNzQiLCJhIjoiY2pnbWdubXR0MjNkazMzbDRtOG44ZWpoeiJ9.rJj_RX53gHN5DXEypqNUfQ'
gmaps = googlemaps.Client(key = "AIzaSyCZKA987rxT9_YYzlIPgtk1iBCT2w3kZsQ")


data = Data([
    Scattermapbox(
        lat = latitude_list,
        lon = longitude_list,
        mode='markers',
        marker=Marker(
            size=9
        ),
        text = names,
        )
])
layout = Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=43.0392,
            lon=-76.1351
        ),
        pitch=0,
        zoom=13
    ),
)

fig = dict(data=data, layout=layout)
py.plot(fig, filename='Multiple Mapbox')


