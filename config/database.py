from pymongo import MongoClient

client = MongoClient("mongodb+srv://tdgroup2023:tdgroup2023@cluster0.xynl9rc.mongodb.net/?retryWrites=true&w=majority")

db = client.simcard

collection_name = db["simcard"]

