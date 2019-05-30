# -*- coding: utf-8 -*-
from datetime import datetime

from scrap import *
from rss.pika import Pika
import click


def group_by(dict_list, key):
    tmp = dict()
    for item in dict_list:
        if not tmp.get(item[key]):
            tmp[item[key]] = []
        tmp[item[key]].append(item)
    return tmp


def print_data(dict_list, reverse):
    grouped_by = group_by(dict_list, 'date')
    for date in sorted(grouped_by.items(), key=lambda x: datetime.strptime(x[0], '%d/%m/%Y'), reverse=reverse):
        for item in grouped_by[date[0]]:
            print("%s\n" % item)


default_editor = ["Glenat", "Kaze", "Kana", "Pika"]


@click.command()
@click.option('--editor', '-e', default=default_editor,
              help='Choose your editor can be multiple resources available(%s)' % default_editor,
              type=click.Choice(default_editor), multiple=True)
@click.option('--reverse', '-r', is_flag=True, default=True, help='reverse the date sort')
def schega(editor, reverse):
    res = []
    if editor:
        default_editor = list(editor)
    for x in range(len(default_editor)):
        default_editor[x] = eval(default_editor[x])
    for x in default_editor:
        res.extend(x().res)
    print_data(res, reverse)


if __name__ == '__main__':
    schega()
