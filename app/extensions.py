from pymongo import MongoClient


client = MongoClient("mongodb+srv://ss:root@dev-cluster.rtbrc.mongodb.net/test")
db = client["dev-cluster"]
collection = db["tech_stax"]


def get_all_extensions():
    return collection.find({})


def insert_extension(data):
    collection.insert_one(data)
