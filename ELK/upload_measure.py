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

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4) # retrieve data from DHT11 sensor
    datetime_object = datetime.datetime.now()
    print('{} | Temp = {0:0.1f} C Humidity: {1:0.1f} %'.format(datetime_object, temperature, humidity))