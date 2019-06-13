from reddit import get_reddit_posts
from api import insert_posts, get_posts_by_source_id, delete_posts_by_source_id
from config import *
from datetime import datetime
import logging
from logs.config import logger

def find_post_in_list(test_post, existing_posts):
    for post in existing_posts:
        if test_post['id'] == post['id']:
            return post


def write_and_update_posts(recent_posts_data, existing_posts_data):

    posts_to_write = []
    posts_to_update = []

    for recent_post in recent_posts_data:
        existing_post = find_post_in_list(recent_post, existing_posts_data)

        if existing_post == None:
            posts_to_write.append(recent_post)

        elif existing_post['source_score'] != recent_post['source_score']:
            posts_to_update.append(recent_post)

    update_ids = [post['id'] for post in posts_to_update]

    print('Writing ' + str(len(posts_to_write)) + ' new posts...')
    print('Updating ' + str(len(posts_to_update)) + ' existing posts...')

    insert_posts(posts_to_write)
    delete_posts_by_source_id(update_ids)
    insert_posts(posts_to_update)


recent_posts_data = get_reddit_posts(REDDIT_CONFIG['test_subreddits'], 100)
recent_ids = [post['id'] for post in recent_posts_data]
existing_posts_data = get_posts_by_source_id(recent_ids)

write_and_update_posts(recent_posts_data, existing_posts_data)
