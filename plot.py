import matplotlib.pyplot as plt


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

