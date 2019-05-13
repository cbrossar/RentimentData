from reddit import *
from api import *


get_crypto_posts()
get_investing_posts()

print('\n---------------\n')

print('Get posts from reddit...')
post1 = get_post1()
post2 = get_post2()

print('Send post data to mongo...')
insert_post(post1)
insert_post(post2)

print('Get posts from mongo...')
posts = get_posts()

print('Posts:')
for post in posts:
    print(post)
    delete_post(post['_id'])