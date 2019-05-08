from db import db
from bson.objectid import ObjectId

# database collections
data = db.data
entities = db.entities


def get_posts():
    return entities.find()


def get_post(post_id):
    return entities.find_one({'_id': ObjectId(post_id)})


def insert_post(post_data):
    return entities.insert(post_data)


def insert_posts(posts_data):
    return entities.insert_many(posts_data)


def delete_post(post_id):
    return entities.delete_one({'_id': ObjectId(post_id)})
