from db import db
from bson.objectid import ObjectId

# database collections
data = db.data
posts = db.posts


def get_posts():
    return posts.find()


# returns None is post is not found
def get_post(post_id):
    return posts.find_one({'_id': ObjectId(post_id)})


# returns None is post is not found
def get_post_by_source_id(source_id):
    return posts.find_one({'id': source_id})


def insert_post(post_data):
    return posts.insert(post_data)


def insert_posts(posts_data):
    return posts.insert_many(posts_data)


def delete_post(post_id):
    return posts.delete_one({'_id': ObjectId(post_id)})
