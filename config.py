MONGO_URL = 'mongodb://admin:password3@ds235197.mlab.com:35197/heroku_gk05lzsb'
DB_NAME = 'heroku_gk05lzsb'

PRAW_CLIENT_ID='L43VTA7AmAw1Qw'
PRAW_SECRET='lKPnAWBKBGRpta-au8GaWylHV2c'

FILES = dict(sentiment_dict='files/sentiwords.txt')

# looking for at least 100k members
REDDIT_CONFIG = dict(crypto_subreddits=['CryptoCurrency', 'CryptocurrencyICO', 'CryptoMarkets', 'investing'],
                     bitcoin_subreddits=['Bitcoin', 'BitcoinMarkets'],
                     ethereum_subreddits=['ethtrader', 'ethereum'],
                     investing_subreddits=['investing', 'wallstreetbets', 'stocks'],
                     all_subreddits=['CryptoCurrency', 'CryptocurrencyICO', 'CryptoMarkets', 'investing', 'Bitcoin',
                                     'BitcoinMarkets', 'ethtrader', 'ethereum', 'wallstreetbets', 'stocks'],
                     test_subreddits=['CryptoMarkets'])

CRYPTO_SYMBOLS = dict(crypto=['crypto', 'cryptocurrency'],
                      btc=['btc', 'bitcoin'],
                      eth=['eth', 'ethereum'],
                      ltc=['ltc', 'litecoin'])


BIZ_SYMBOLS = dict(amzn=['amzn', 'amazon'],
                   goog=['goog', 'google', 'alphabet'])
