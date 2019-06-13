from sentiment import build_sentiment_dictionary, get_sentiment_score, tokenize
from datetime import datetime
import json

def load_all_subjects():
    with open('./files/subjects.json') as f:
        return json.load(f)


def get_target_subject(tokens, target_subjects, type='stocks'):

    target = None
    for token in tokens:
        for key in target_subjects[type]:
            if token.lower() in target_subjects[type][key] or token.lower().replace('$', '') == key:
                target = key
    return target


def create_reddit_post_dictionary(submission, subreddit, sentiment_dict):

    all_subjects = load_all_subjects()
    all_tokens = tokenize(submission.title) + tokenize(submission.selftext)

    return dict(id=submission.id,
                source='reddit',
                sub_source=subreddit.display_name,
                content_type='post',
                author=submission.author.name if submission.author is not None else None,
                title=submission.title,
                text=submission.selftext,
                title_sentiment=get_sentiment_score(submission.title, sentiment_dict),
                text_sentiment=get_sentiment_score(submission.selftext, sentiment_dict),
                subject=get_target_subject(all_tokens, all_subjects),
                source_score=submission.score,
                upvote_ratio=submission.upvote_ratio,
                num_comments=submission.num_comments,
                parent=None,
                publish_date=datetime.utcfromtimestamp(submission.created_utc))
