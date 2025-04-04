from pymongo import MongoClient


client = MongoClient("mongodb://myuser:mypassword@localhost:27017/user-account")

db = client["user-account"]
print("Connected successfully!")