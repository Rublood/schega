from datetime import datetime

import feedparser


class Pika:
    domain = "http://pika.fr"
    url = ["http://www.pika.fr/rss/collection/4/rss.xml",
           "http://www.pika.fr/rss/collection/5/rss.xml",
           "http://www.pika.fr/rss/collection/7/rss.xml",
           "http://www.pika.fr/rss/collection/9/rss.xml"]
    res = []
    html = False
    timeline = False
    stop_loop = False

    def add_item(self, item):
        var = {
            'name': self.format_name(item.title),
            'date': datetime.strptime(item.description, 'Date de parution : %d/%m/%Y').strftime('%d/%m/%Y'),
            'link': item.link,
            'editor': 'pika'
        }
        self.res.append(var)

    def __init__(self, **kwargs):
        super(Pika, self)
        for cat in self.url:
            rss = feedparser.parse(cat)
            for item in rss.entries:
                self.add_item(item)

    def format_name(self, name):
        name = name.rsplit(' ', 1)
        name = str(name[0] + " - " + name[1])
        return name
