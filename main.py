from api import get_posts_by_date_range
from datetime import datetime
import logging
from plot import plot_count_by_hour, plot_sentiment_by_hour

logger = logging.getLogger('Rentiment.' + __name__)

start = datetime(2019, 7, 1, 0, 0, 0)
end = datetime(2019, 7, 17, 0, 0, 0)

logger.info('Get posts from ' + str(start) + ' to ' + str(end))
posts = get_posts_by_date_range(start, end)

plot_count_by_hour('Rentiment Posts', posts)

# plot_sentiment_by_hour('Rentiment Sentiment', posts)

