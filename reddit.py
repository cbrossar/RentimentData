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

def get_post1():
    post_data = {'source': 'Reddit', 'author': 'Bob', 'content': 'Bitcoin sucks', 'type': 'post'}
    return post_data


def get_post2():
    post_data = {'source': 'Reddit', 'author': 'Joe', 'content': 'Bitcoin is going to the moon', 'type': 'post'}
    return post_data