#!/usr/bin/python
import os
import sys
import datetime
import requests
import Adafruit_DHT

from dotenv import load_dotenv

# Find the dotenv in the current directory
load_dotenv()

API_KEY     = os.getenv('TS_API_KEY_WRITE')

# retrieve data from DHT11 sensor
humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print('Temp = {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))

base_url = 'https://api.thingspeak.com/update?api_key=' + API_KEY
url_1 = base_url + '&field1=' + str(humidity)
url_2 = base_url + '&field2=' + str(temperature)

res = requests.get(url_1)
print(res)

res = requests.get(url_2)
print(res)



