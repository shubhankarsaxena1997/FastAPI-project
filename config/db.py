from pymongo import MongoClient
import os
from dotenv import load_dotenv

# load .env file to environment
load_dotenv()

MONGO_URI = os.getenv("connectionString")

conn = MongoClient(MONGO_URI)
