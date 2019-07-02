# looking for at least 100k members
REDDIT_CONFIG = dict(crypto_subreddits=['CryptoCurrency', 'CryptocurrencyICO', 'CryptoMarkets', 'investing'],
                     bitcoin_subreddits=['Bitcoin', 'BitcoinMarkets'],
                     ethereum_subreddits=['ethtrader', 'ethereum'],
                     investing_subreddits=['investing', 'wallstreetbets', 'stocks'],
                     test_subreddits=['investing'],
                     all_subreddits=['CryptoCurrency', 'CryptocurrencyICO', 'CryptoMarkets', 'investing', 'Bitcoin',
                                     'BitcoinMarkets', 'ethtrader', 'ethereum', 'wallstreetbets', 'stocks'])

FILES = dict(sentiment_dict='files/sentiwords.txt')

# Todo: choose a strategy. Can also put in separate json file
# Strategy 1
SYMBOLS = dict(btc=dict(name='Bitcoin', type='cryptocurrency', keywords=['btc', 'bitcoin']),
               eth=dict(name='Ethereum', type='cryptocurrency', keywords=['eth', 'ethereum']),
               amzn=dict(name='Amazon', type='business', keywords=['amzn', 'amazon']),
               goog=dict(name='Alphabet Inc.', type='business', keywords=['goog', 'google', 'alphabet']))

# Strategy 2
SYMBOLS = dict(btc=['btc', 'bitcoin'],
               eth=['eth', 'ethereum'],
               amzn=['amzn', 'amazon'],
               goog=['goog', 'google', 'alphabet'])

CRYPTO_SYMBOLS = dict(btc=['btc', 'bitcoin'],
                      eth=['eth', 'ethereum'])

# Strategy 3
BIZ_SYMBOLS = dict(amzn=['amzn', 'amazon'],
                   goog=['goog', 'google', 'alphabet'])
