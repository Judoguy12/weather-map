from requests import get
import webbrowser
import folium
import os

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getalllastmeasurement'

station_data = get(url).json()


