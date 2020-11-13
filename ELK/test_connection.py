import os

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

res = es.search(index='gang-news', filter_path=['hits.hits._id', 'hits.hits._type'])

print(res)
