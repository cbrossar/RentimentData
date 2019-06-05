from sentiment import build_sentiment_dictionary, get_sentiment_score
from datetime import datetime


def create_reddit_post_dictionary(submission, subreddit):

    sentiment_dict = build_sentiment_dictionary()
    return dict(id=submission.id,
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
                publish_date=datetime.utcfromtimestamp(submission.created_utc))
