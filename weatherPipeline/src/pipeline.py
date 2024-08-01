# WARNING: JUST FOR DEVELOPMENT PURPOSES, NEVER NEVER NEVER WRITING ANY KEY INSIDE THE CODE BASE OR PLAIN TEXT!!!!
import requests
from datetime import datetime
import os
import sys
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
sys.path.append(data_dir)
import database as db



# ==========
# EXTRACTION

api_key = "53f3e4272508b6d9a59652a28b4c7e3a"
city = "London"
site_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)


# We do the GET 
try:
    response = requests.get(site_url)
    data = response.json()

except requests.exceptions.RequestException as e:
    raise e
    exit()


# ==============
# TRANSFORMATION

city_name = data["name"]
temp = data['main']['temp']
weather_description = data['weather'][0]['description']
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Showing transformed data
#print("City:{}, Temperature{}C, Weather: {}, Time:{}".format(city_name, temp, weather_description, timestamp))


# ==============
# LOAD
db.load_data(city_name, temp, weather_description, timestamp)
