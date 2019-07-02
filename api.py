from db import db
from bson.objectid import ObjectId

# database collections
data = db.data
posts = db.posts


def test_db_connection():
    return True


def get_posts():
    return list(posts.find())


def get_post_ids():
    post_ids = list(posts.find({}, {'_id': 0, 'id': 1}))
    post_ids = [p['id'] for p in post_ids]
    return post_ids


# returns None is post is not found
def get_post(post_id):
    return posts.find_one({'_id': ObjectId(post_id)})


# returns None is post is not found
def get_post_by_source_id(source_id):
    test = posts.find_one({'id': source_id})
    return test


# returns None if no posts are found
def get_posts_by_source_id(source_ids):
    return list(posts.find({'id': { '$in': source_ids }}))


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


def write_and_update_posts(posts_data, existing_ids):
    update_ids = []

    for post in posts_data:
        if post['id'] in existing_ids:
            update_ids.append(post['id'])

    delete_posts_by_source_id(update_ids)
    insert_posts(posts_data)


def delete_post(post_id):
    return posts.delete_one({'_id': ObjectId(post_id)})


def delete_posts_by_source_id(post_ids):
    return posts.delete_many({'id': {'$in': post_ids}})
