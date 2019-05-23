from reddit import *
from api import *
from config import *


print('Get posts from reddit...')
posts_data = get_reddit_posts(REDDIT_CONFIG['test_subreddits'])

print('Insert posts into mongo...')
insert_posts(posts_data)

print('Get posts from mongo...')
posts = get_posts()

print('Posts:')
for post in posts:
    print(post)
    # delete_post(post['_id'])

