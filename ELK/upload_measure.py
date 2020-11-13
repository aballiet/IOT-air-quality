#!/usr/bin/python
import os
import sys
import Adafruit_DHT
import datetime

from dotenv import load_dotenv, find_dotenv
from elasticsearch import Elasticsearch

# Find the dotenv in the current directory
load_dotenv()

ELK_USER     = os.getenv('ELK_USER')
ELK_PASSWORD = os.getenv('ELK_PASSWORD')

HOST      = os.getenv('ELK_HOST')
PORT      = os.getenv('ELK_PORT')
HTTP_AUTH = ELK_USER + ':' + ELK_PASSWORD

print('Connecting to ' + HOST + ':' + PORT)

# Create the ElasticSearch connector instance
es = Elasticsearch([{
    'host': HOST,
    'port': PORT
    }],
    http_auth=HTTP_AUTH
)

index = 'gang-sensor-test'

while True:
    # retrieve data from DHT11 sensor
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    # Nicely print measure
    datetime_object = datetime.datetime.now().isoformat()
    print(str(datetime_object) + '| Temp = {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))

    # create JSON data to upload to ElasticSearch
    data = {
        "@timestamp": str(datetime_object),
        "humidity": humidity,
        "temperature": temperature,
        "room": 'Antoine'
    }

    json_dump = json.dumps(data)
    #print(json_dump)

    # Upload Data
    res = es.index(index=index, body=json_dump)
    print(res['result'])