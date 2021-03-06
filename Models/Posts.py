import pymongo, bcrypt
from pymongo import MongoClient


class Posts:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.devtalk
        self.Users = self.db.users
        self.Posts = self.db.posts


    def insert_post(self, data):
        inserted = self.Posts.insert({"username": data.username, "content": data.content})
        return True


    def get_all_posts(self):
        new_posts = []
        all_posts = self.Posts.find()

        for post in all_posts:
            post["user"] = self.Users.find_one({"username": post["username"]})
            new_posts.append(post)

        return new_posts