import praw
from api import *
from sentiment import *

reddit = praw.Reddit('bot1', user_agent='bot1 user agent')


def get_reddit_posts(subreddits, count=1000):

    post_data = []
    sentiment_dict = build_sentiment_dictionary()

    for sub in subreddits:
        subreddit = reddit.subreddit(sub)

        for submission in subreddit.new(limit=count):

            if get_post_by_source_id(submission.id) is None:

                post = dict(id=submission.id,
                            source='reddit',
                            sub_source=subreddit.display_name,
                            content_type='post',
                            author=submission.author.name if submission.author is not None else None,
                            title=submission.title,
                            text=submission.selftext,
                            title_sentiment=get_sentiment_score(submission.title, sentiment_dict),
                            text_sentiment=get_sentiment_score(submission.selftext, sentiment_dict),
                            source_score=submission.score,
                            upvote_ratio=submission.upvote_ratio,
                            num_comments=submission.num_comments,
                            parent=None,
                            publish_date=submission.created_utc)

                post_data.append(post)

    return post_data
