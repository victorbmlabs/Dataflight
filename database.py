
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from ryanair.types import Flight
from dotenv import load_dotenv
from typing import List
import certifi
import os

load_dotenv()
connection_string = os.getenv("MONGO_COONNECTION_STRING")
db = os.getenv("MONGO_DB")
collection = os.getenv("MONGO_COLLECTION")

if all([connection_string, db, collection]) is False:
    raise Exception("Missing environment variables")

# Create a new client and connect to the server
client = MongoClient(connection_string, server_api=ServerApi('1'), tlsCAFile=certifi.where())
db = client[db]
ryanair_oneways = db[collection]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Sucessfully connected to MongoDB!")
except Exception as e:
    print(e)

def add_ryanair_flights(flights: List[dict]):
    ryanair_oneways.insert_many(flights)
