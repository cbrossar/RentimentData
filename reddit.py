# from sentiment import analyze sentiment
import praw
from config import *

reddit = praw.Reddit('bot1', user_agent='bot1 user agent')


def get_crypto_posts():

    for sub in REDDIT_CONFIG['crypto_subreddits']:
        subreddit = reddit.subreddit(sub)
        print("\n" + subreddit.display_name)

        for submission in subreddit.hot(limit=10):
            print(submission.title)


def get_investing_posts():

    for sub in REDDIT_CONFIG['investing_subreddits']:
        subreddit = reddit.subreddit(sub)
        print("\n" + subreddit.display_name)

        for submission in subreddit.hot(limit=10):
            print(submission.title)
