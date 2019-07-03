import praw
from config import *
from utility import create_reddit_post_dictionary
from sentiment import build_sentiment_dictionary
import logging
import json

logger = logging.getLogger('Rentiment.' + __name__)
reddit = praw.Reddit(client_id=PRAW_CLIENT_ID, client_secret=PRAW_SECRET, user_agent='bot1 user agent')


def get_reddit_posts(subreddits, count=1000):

    # Build sentiment dictionary here so we don't build it for every posts
    sentiment_dict = build_sentiment_dictionary()

    post_data = []
    for sub in subreddits:
        subreddit = reddit.subreddit(sub)
        logger.info('Searching the following subreddit: ' + str(sub))

        for submission in subreddit.new(limit=count):
            post = create_reddit_post_dictionary(submission, subreddit, sentiment_dict)
            post_data.append(post)

    return post_data
