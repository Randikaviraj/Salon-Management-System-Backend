from pymongo import MongoClient
from Server.config import MONGO_PORT,MONGO_HOST

client = MongoClient(MONGO_HOST, MONGO_PORT)

db = client['saloon']

