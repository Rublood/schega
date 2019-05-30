# -*- coding: utf-8 -*-
from datetime import datetime

from scrap import *
from rss.pika import Pika


def group_by(dict_list, key):
    tmp = dict()
    for item in dict_list:
        if not tmp.get(item[key]):
            tmp[item[key]] = []
        tmp[item[key]].append(item)
    return tmp


def print_data(dict_list):
    grouped_by = group_by(dict_list, 'date')
    for date in sorted(grouped_by.items(), key=lambda x: datetime.strptime(x[0], '%d/%m/%Y'), reverse=True):
        for item in grouped_by[date[0]]:
            print("%s\n" % item)


editor = [Glenat, Kaze, Kana, Pika]
res = []
for x in editor:
    res.extend(x().res)
print_data(res)
