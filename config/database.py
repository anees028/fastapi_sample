from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@cluster0.4hcfhiv.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_collection"]


