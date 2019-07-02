import matplotlib.pyplot as plt
from datetime import timedelta


def plot(title, x_label, y_label, posts):

    x = []
    y = []

    for post in posts:
        x.append(post[x_label])
        y.append(post[y_label])

    plt.plot_date(x, y)
    plt.gcf().autofmt_xdate()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def plot_by_hour(title, y_label, posts):

    hour_count = dict()

    for post in posts:
        post_time = post[y_label].replace(minute=0, second=0)
        if post_time in hour_count:
            hour_count[post_time] += 1
        else:
            hour_count[post_time] = 1

    plt.plot_date(list(hour_count.keys()), list(hour_count.values()))
    plt.gcf().autofmt_xdate()
    plt.title(title)
    plt.xlabel('publish hour')
    plt.ylabel('count')
    plt.show()
