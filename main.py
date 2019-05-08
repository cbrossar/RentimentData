from reddit import *
from api import *


print('Get posts from reddit...')
post1 = get_post1()
post2 = get_post2()
post3 = get_post3()
post4 = get_post4()

posts_data = list()
posts_data.append(post1)
posts_data.append(post2)
posts_data.append(post3)
posts_data.append(post4)

print('Send post data to mongo...')
insert_posts(posts_data)

print('Get posts from mongo...')
posts = get_posts()

print('Posts:')
for post in posts:
    print(post)
    delete_post(post['_id'])

