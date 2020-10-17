from datetime import datetime

#from bson import ObjectId
from pymongo import MongoClient, DESCENDING
#from werkzeug.security import generate_password_hash


client = MongoClient()#enter db connection

chatdb = client.get_database("teachers")
user_collection = chatdb.get_collection("users")
rooms_collection = chatdb.get_collection("rooms")
message_collection = chatdb.get_collection("messages")


def save_message(room_id, text, sender):
    message_collection.insert_one({'room_id':room_id, 'text' : text, 'sender': sender})

def get_message(room_id,count):
    messages = list(message_collection.find({'room_id': room_id}))
    return messages
