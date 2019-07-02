from config import CRYPTO_SYMBOLS
from sentiment import get_sentiment_score, tokenize
from datetime import datetime


def get_target_subjects(tokens):
    targets = []
    for token in tokens:
        for key in CRYPTO_SYMBOLS:
            if token.lower() in CRYPTO_SYMBOLS[key]:
                targets.append(key)
    return list(set(targets))


def create_reddit_post_dictionary(submission, subreddit, sentiment_dict):

    tokens = tokenize(submission.title) + tokenize(submission.selftext)

    return dict(id=submission.id,
                source='reddit',
                sub_source=subreddit.display_name,
                content_type='post',
                author=submission.author.name if submission.author is not None else None,
                title=submission.title,
                text=submission.selftext,
                title_sentiment=get_sentiment_score(submission.title, sentiment_dict),
                text_sentiment=get_sentiment_score(submission.selftext, sentiment_dict),
                subjects=get_target_subjects(tokens),
                source_score=submission.score,
                upvote_ratio=submission.upvote_ratio,
                num_comments=submission.num_comments,
                parent=None,
                publish_date=datetime.utcfromtimestamp(submission.created_utc))
