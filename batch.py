from reddit import get_reddit_posts
from api import get_post_ids, write_and_update_posts
from config import *
import logging
from logs.config import logger

logger.info('Setup logger')
logger = logging.getLogger('Rentiment.' + __name__)


logger.info('Get posts from reddit...')
posts_data_l = get_reddit_posts(REDDIT_CONFIG['large_crypto_subs'], 100)
posts_data_s = get_reddit_posts(REDDIT_CONFIG['small_crypto_subs'], 100)


logger.info('Insert posts into mongo...')
existing_ids = get_post_ids()
write_and_update_posts(posts_data_l, existing_ids)
write_and_update_posts(posts_data_s, existing_ids)
