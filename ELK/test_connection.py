import os

from dotenv import load_dotenv, find_dotenv
from elasticsearch import Elasticsearch

# Find the dotenv in the current directory
load_dotenv()

ELK_USER     = os.getenv('ELK_USER')
ELK_PASSWORD = os.getenv('ELK_PASSWORD')
INDEX        = os.getenv('ELK_INDEX')

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

res = es.cat.count(INDEX, params={"format": "json"})
print("Count: {}".format(res[0]["count"]))