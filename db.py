from pymongo import MongoClient
from config import MONGO_URL, DB_NAME

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

# uncomment below to connect to local mongodb instance
# client = MongoClient()
# db = client.rentiment
