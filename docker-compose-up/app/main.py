from pymongo import MongoClient
from pprint import pprint

MONGO_URL = "mongodb://mongo:27017"
client=MongoClient(MONGO_URL)
db= client.admin
dbe_list = db.command("listDatabases")
pprint(dbe_list)