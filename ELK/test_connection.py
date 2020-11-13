import os

from dotenv import load_dotenv, find_dotenv
from elasticsearch import Elasticsearch

# Find the dotenv in the current directory
load_dotenv()

ELK_USER     = os.getenv("USER")
ELK_PASSWORD = os.getenv('PASSWORD')

HOST      = os.getenv("HOST")
PORT      = os.getenv('PORT')
HTTP_AUTH = ELK_USER + ':' + ELK_PASSWORD

print("Connecting to " + HOST + PORT)
print(HTTP_AUTH)

# Create the ElasticSearch connector instance
es = Elasticsearch([{
    'host': HOST,
    'port': PORT
    }],
    http_auth=HTTP_AUTH
)

res = es.search(index='gang-news', filter_path=['hits.hits._id', 'hits.hits._type'])

print(res)
