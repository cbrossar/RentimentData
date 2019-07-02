from reddit import get_reddit_posts
from api import insert_posts, get_posts, get_posts_by_date_range, get_posts_by_subreddit
from config import *
from datetime import datetime
import logging
from logs.config import logger
from plot import plot, plot_by_hour

# logger.info('Setup logger')
# logger = logging.getLogger('Rentiment.' + __name__)
#
# logger.info('Get posts from reddit...')
# posts_data = get_reddit_posts(REDDIT_CONFIG['all_subreddits'])
#
# logger.info('Insert posts into mongo...')
# insert_posts(posts_data)

logger.info('Get posts from mongo...')
posts = get_posts()

logger.debug('Posts:')
for post in posts:
    logger.debug(post)

start = datetime(2019, 6, 2, 0, 0, 0)
end = datetime(2019, 7, 1, 0, 0, 0)

logger.info('Get posts from ' + str(start) + ' to ' + str(end))

posts = get_posts_by_subreddit('Bitcoin')

# plot('Rentiment Bitcoin', 'publish_date', 'text_sentiment', posts)

# plot_by_hour('Rentiment Bitcoin', 'publish_date', posts)
