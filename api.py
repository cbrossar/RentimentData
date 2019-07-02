from db import db
from bson.objectid import ObjectId
from datetime import datetime

# database collections
data = db.data
posts = db.posts


def test_db_connection():
    return True


def get_posts():
    return posts.find()


# returns None is post is not found
def get_post(post_id):
    return posts.find_one({'_id': ObjectId(post_id)})


# returns None is post is not found
def get_post_by_source_id(source_id):
    return posts.find_one({'id': source_id})


def get_posts_by_date_range(start, end):
    return posts.find({'publish_date': {'$lt': end, '$gte': start}})


def get_posts_by_subreddit(subreddit):
    return posts.find({'sub_source': subreddit})


def insert_post(post_data):
    if post_data:
        return posts.insert(post_data)


def insert_posts(posts_data):
    if posts_data:
        return posts.insert_many(posts_data)


def delete_post(post_id):
    return posts.delete_one({'_id': ObjectId(post_id)})


