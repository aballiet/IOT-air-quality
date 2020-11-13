#!/usr/bin/python
import os
import sys
import Adafruit_DHT
import datetime
import json

from dotenv import load_dotenv, find_dotenv
from elasticsearch import Elasticsearch

# Find the dotenv in the current directory
load_dotenv()

ELK_USER     = os.getenv('ELK_USER')
ELK_PASSWORD = os.getenv('ELK_PASSWORD')

HOST = os.getenv('ELK_HOST')
PORT = os.getenv('ELK_PORT')

INDEX            = os.getenv('ELK_INDEX')
ELK_LOCATION_LAT = os.getenv('ELK_LOCATION_LAT')
ELK_LOCATION_LON = os.getenv('ELK_LOCATION_LON')
ROOM             = os.getenv('ELK_ROOM')

HTTP_AUTH = ELK_USER + ':' + ELK_PASSWORD

# Build formatted location for GeoPoint type
LOCATION = [float(ELK_LOCATION_LAT), float(ELK_LOCATION_LON)]

print('Connecting to ' + HOST + ':' + PORT)

# Create the ElasticSearch connector instance
es = Elasticsearch([{
    'host': HOST,
    'port': PORT
    }],
    http_auth=HTTP_AUTH
)

while True:
    # retrieve data from DHT11 sensor
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    # Nicely print measure
    datetime_object = datetime.datetime.now().isoformat()
    #print(str(datetime_object) + '| Temp = {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))

    # create JSON data to upload to ElasticSearch
    data = {
        "@timestamp": str(datetime_object),
        "humidity": humidity,
        "temperature": temperature,
        "location": LOCATION,
        "room": ROOM
    }

    json_dump = json.dumps(data)
    print(json_dump)

    # Upload Data
    res = es.index(index=INDEX, doc_type='demo', body=json_dump)
    print(res['result'])