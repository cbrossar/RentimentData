import praw
from api import *

reddit = praw.Reddit('bot1', user_agent='bot1 user agent')


def get_reddit_posts(subreddits):

    post_data = []

    for sub in subreddits:
        subreddit = reddit.subreddit(sub)

        for submission in subreddit.new(limit=1000):

            if get_post_by_source_id(submission.id) is None:

                post = dict(id=submission.id,
                            source='reddit',
                            sub_source=subreddit.display_name,
                            author=submission.author.name if submission.author is not None else None,
                            title=submission.title,
                            text=submission.selftext,
                            content_type='post',
                            sentiment=0,
                            score=submission.score,
                            upvote_ratio=submission.upvote_ratio,
                            num_comments=submission.num_comments,
                            parent=None,
                            publish_date=submission.created_utc)

                post_data.append(post)

    return post_data
