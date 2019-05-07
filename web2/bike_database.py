from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb+srv://admin:admin@namnguyen-ch7mo.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)

bike_db = client.bike_database

bike_collection = bike_db["bike_collection"]

bike = [
{
        "model" : "Honda SH",
        "fee" : "500000",
        "link" : "https://imgwebikevn-8743.kxcdn.com/58C4wYg8eEPyCW_2YlmSIoIfA6c=/product/2018/08/04/wvn.05b65182a13dc02.48439864.jpg",
        "year": 2009
},
{
        "model" : "Honda Spacy",
        "fee" : "300000",
        "link" : "https://image.anninhthudo.vn/w700/uploaded/caominh/2011_09_05/spacy.jpg",
        "year" : 2005
}
]

# bike_collection.insert_many(bike)