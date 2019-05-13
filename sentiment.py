import re

def get_sentiment_dictionary():
    sentiwords_dict = {}
    sentiwords = open('config/sentiwords.txt', 'r')
    for line in sentiwords.readlines():
        columns = re.split('#[a-z]', line.replace('\n', '').replace('\t', ''))
        if len(columns) > 1:
            sentiwords_dict[columns[0]] = float(columns[1])
    return sentiwords_dict

def get_sentiment_score(string, sentiment_dict):
    sentiment = 0
    word_list = re.sub('[^\w]', ' ', string).split()
    for word in word_list:
        if word in sentiment_dict:
            sentiment += sentiment_dict[word]
    return sentiment
