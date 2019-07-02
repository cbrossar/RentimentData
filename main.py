from reddit import get_reddit_posts
from api import get_posts, get_post_ids, write_and_update_posts, get_posts_by_subreddit
from config import *
from datetime import datetime
import logging
from logs.config import logger
from plot import plot, plot_by_hour

logger.info('Setup logger')
logger = logging.getLogger('Rentiment.' + __name__)


logger.info('Get posts from reddit...')
posts_data = get_reddit_posts(REDDIT_CONFIG['test_subreddits'], 20)

logger.info('Insert posts into mongo...')
existing_ids = get_post_ids()
write_and_update_posts(posts_data, existing_ids)

logger.info('Get posts from mongo...')
posts = get_posts()


start = datetime(2019, 6, 2, 0, 0, 0)
end = datetime(2019, 7, 1, 0, 0, 0)

logger.info('Get posts from ' + str(start) + ' to ' + str(end))

posts = get_posts_by_subreddit('Bitcoin')

# plot('Rentiment Bitcoin', 'publish_date', 'text_sentiment', posts)

plot_by_hour('Rentiment Bitcoin', 'publish_date', posts)
