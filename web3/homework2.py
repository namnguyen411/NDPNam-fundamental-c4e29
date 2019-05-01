from pymongo import MongoClient
from bson.objectid import ObjectId

uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(uri)

data = client.c4e

river = data.river

# Africa_river = river.find({'continent':'Africa'})

# for river in Africa_river:
#     print(river['name']) 

S_America_river = river.find({'continent':'S. America'})

for river in S_America_river:
    if (river['length'] > 1000):
        print(river['name'])