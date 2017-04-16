import pymongo
import bcrypt
from pymongo import MongoClient


class RegisterModel:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.devtalk
        self.Users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())

        id = self.Users.insert({"username": data.username, "name": data.name, "password": hashed, "email": data.email})
        print("UID is", id)

        my_user = self.Users.find_one({"username": data.username})

        if bcrypt.checkpw("Test123".encode(), my_user["password"]):
            print("Passwords match.")

