import re
import nltk
from nltk.tag import pos_tag, map_tag

def build_sentiment_dictionary():
    sentiwords_dict = {}
    sentiwords = open('config/sentiwords.txt', 'r')
    for line in sentiwords.readlines():
        pos = re.findall('#[a-z]', line)
        columns = re.split('#[a-z]', line.replace('\n', '').replace('\t', ''))
        if len(columns) > 1 and len(pos) > 0:
            if columns[0] not in sentiwords_dict:
                sentiwords_dict[columns[0]] = {}
            sentiwords_dict[columns[0]][pos[0]] = float(columns[1])
    return sentiwords_dict

def lookup_sentiment_score(word, part_of_speech, sentiment_dict):
    if word in sentiment_dict:
        options = sentiment_dict[word]
        pos_simple = '#' + part_of_speech[0].lower()
        if pos_simple in options:
            return sentiment_dict[word][pos_simple]
    return 0

def get_sentiment_score(string, sentiment_dict):
    sentiment = 0
    tokens = nltk.word_tokenize(string)
    parts_of_speech = nltk.pos_tag(tokens)
    simplified_tags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in parts_of_speech]
    for token in simplified_tags:
        sentiment += lookup_sentiment_score(token[0], token[1], sentiment_dict)
    return sentiment
